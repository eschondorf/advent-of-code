function solver(arr, part2 = false)
    rv = 0
    if ! part2
        for line in arr
            card_num, win_lst, num_lst = parse_line(line)
            win_set = Set(win_lst)
            num_set = Set(num_lst)
            if length(win_set)!= length(win_lst)
                error("Wrong sizes!")
            end
            if length(num_set)!= length(num_lst)
                error("Wrong sizes!")
            end
            winning_nums = intersect(win_set, num_set)
            if length(winning_nums) != 0
                rv += 2^(length(winning_nums)-1)
            end
        end
    end
    if part2
        pts_lst = []
        for line in arr
            tmp = 0
            card_num, win_lst, num_lst = parse_line(line)
            win_set = Set(win_lst)
            num_set = Set(num_lst)
            if length(win_set)!= length(win_lst)
                error("Wrong sizes!")
            end
            if length(num_set)!= length(num_lst)
                error("Wrong sizes!")
            end
            winning_nums = intersect(win_set, num_set)
            if length(winning_nums) != 0
                tmp = 2^(length(winning_nums)-1)
            end
            tpl = [tmp, winning_nums]
            push!(pts_lst, tmp)
        end
        for i in 1:length(pts_lst)
            rv += win_cards(pts_lst, i)
        end

    end
   return rv
end


function win_cards(pts_lst, i)
    if pts_lst[i] == 0
        return 1
    else
        rv = 1
        cards_ahead = Int(log2(pts_lst[i])) + 1
        for j in 1: cards_ahead
            rv += win_cards(pts_lst, i+j)
        end
        return rv
    end

    
end


function parse_line(line)
    card_str, win_str, num_str = split(line, (':', '|'))
    card_num = parse(Int, split(card_str, ' ')[end])
    win_lst = split(win_str) |> x -> parse.(Int, x)
    num_lst = split(num_str) |> x -> parse.(Int, x)    
    return card_num, win_lst, num_lst
end

function winning_nums(win_set, num_set)
    rv = []
    for elt in num_lst
        if elt in win_lst
            append!(rv, elt)
        end
    end
    return rv
end



function main()
    f = open("input_files/day_4.txt")
    lines = readlines(f)
    f_test = open("input_files/day_4_test.txt")
    lines_test = readlines(f_test)
    println(solver(lines_test, false))
    println(solver(lines, false))
    println(solver(lines_test, true))
    println(solver(lines, true))



end

main()