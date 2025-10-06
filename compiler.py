def compile_syon_to_cpp(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cpp_code = ['#include <iostream>', 'int main() {']

    for line in lines:
        line = line.strip()
        if line.startswith('출력('):
            content = line[3:].strip('()')
            cpp_code.append(f'    std::cout << {content} << std::endl;')
        elif line == '끝':
            cpp_code.append('    return 0;')
            cpp_code.append('}')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cpp_code))

# 실행 예시
compile_syon_to_cpp('examples/hello.syon', 'output.cpp')
