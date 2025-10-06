# compiler.py
def compile_syon_to_cpp(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cpp_code = ['#include <iostream>', 'int main() {']

    for line in lines:
        line = line.strip()

        # 출력 처리
        if line.startswith('출력('):
            content = line[3:].strip('()')
            cpp_code.append(f'    std::cout << {content} << std::endl;')

        # 변수 선언 처리
        elif line.startswith('변수'):
            parts = line.split('=')
            var_name = parts[0].split('"')[1]
            value = parts[1].strip()
            if '숫자' in value:
                val = value.split('."')[1]
                cpp_code.append(f'    int {var_name} = {val};')
            elif '이름' in value:
                val = value.split('."')[1]
                cpp_code.append(f'    std::string {var_name} = "{val}";')

        # 조건문 처리
        elif line.startswith('만약'):
            condition = line.replace('만약', '').replace(':', '').strip()
            condition = condition.replace('변수."', '').replace('숫자."', '')
            cpp_code.append(f'    if ({condition}) {{')

        elif line.startswith('아니면'):
            cpp_code.append('    } else {')

        # 끝 처리
        elif line == '끝':
            cpp_code.append('    }')

    cpp_code.append('    return 0;')
    cpp_code.append('}')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cpp_code))

# 실행 예시
compile_syon_to_cpp('hello.syon', 'output.cpp')
