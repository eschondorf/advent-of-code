function solver(arr, part2 = false)
    rv = 0
    for i in 1:length(arr)
        rv += get_sum_part_2(arr[i], part2)
        end
    return rv
end


#=
function get_sum(stg, part2)
    first_num = -1
    last_num = -1
    first = false
    if part2
        println(stg)

    for character in stg
        if isdigit(character)
            if !first
                first_num = parse(Int, character)
                first = true
            end
            last_num = parse(Int, character)
        end
    end
    return first_num*10 + last_num
end
=#


function get_sum_part_2(stg, part2)
    return get_first(stg, part2)*10 + get_last(stg, part2)
end


function get_first(stg, part2)
    max_len = length(stg)
    for (i, character) in enumerate(stg)
        if isdigit(character)
            return parse(Int, character)
        end
        if part2
            if character == 't'
                if stg[i:min(i+2, max_len)] == "two" 
                    return 2
                end
                if stg[i:min(i+4, max_len)] == "three" 
                    return 3
                end
            end
            if character == 'o'
                if stg[i:min(i+2, max_len)] == "one" 
                    return 1
                end
            end
            if character == 'f'
                if stg[i:min(i+3, max_len)] == "five" 
                    return 5
                end
                if stg[i: min(i+3, max_len)] == "four"
                    return 4
                end
            end
            if character == 's'
                if stg[i:min(i+2, max_len)] == "six" 
                    return 6
                end
                if stg[i:min(i+4, max_len)] == "seven" 
                    return 7
                end
                
            end
            if character == 'e'
                if stg[i:min(i+4, max_len)] == "eight" 
                    return 8
                end
            end 
            if character == 'n'
                if stg[i:min(i+3, max_len)] == "nine" 
                    return 9
                end
            end
        end
    end
end 


function get_last(stg, part2)
    stg = reverse(stg)
    max_len = length(stg)
    for (i, character) in enumerate(stg)
        if isdigit(character)
            return parse(Int, character)

        end
        if part2
            if character == 'o'
                if reverse(stg[i:min(i+2, max_len)]) == "two" 
                    return 2
                end
                
            end

            if character == 'x'
                if reverse(stg[i:min(i+2, max_len)]) == "six" 
                    return 6
                end
            end
            if character == 'n'
                if reverse(stg[i:min(i+4, max_len)]) == "seven" 
                    return 7
                end
                
            end
            if character == 't'
                if reverse(stg[i:min(i+4, max_len)]) == "eight" 
                    return 8
                end
            end 
            if character == 'r'
                if reverse(stg[i: min(i+3, max_len)]) == "four"
                    return 4
                end
            end
            if character == 'e'
                if reverse(stg[i:min(i+3, max_len)]) == "nine" 
                    return 9
                end
                if reverse(stg[i:min(i+3, max_len)]) == "five" 
                    return 5
                end
                if reverse(stg[i:min(i+4, max_len)]) == "three" 
                    return 3
                end
                if reverse(stg[i:min(i+2, max_len)]) == "one" 
                    return 1
                end
            end
        end
    end
end 



function main()
    f = open("input_files/day_1.txt")
    lines = readlines(f)
    f_test = open("input_files/day_1_test.txt")
    lines_test = readlines(f_test)
    println(solver(lines_test[1:4], false))
    println(solver(lines, false))
    println(solver(lines_test[5:11], true))
    println(solver(lines, true))
end

main()