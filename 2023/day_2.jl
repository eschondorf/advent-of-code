function solver(arr, part2 = false)
    rv = 0
    if ! part2
        for line in arr
            rv += game_valid(line)
        end
    end
    if part2
        for line in arr
            rv += fewest_cubes(line)        
        end
    end
   return rv
end


function game_valid(line)
    game, rslt = split(line, ':')
    round = split(rslt, ';')
    for hand in round
        x = split(hand, ',')
        for blocks in x
            _, num, color = split(blocks, ' ')
            num = parse(Int, num)
            
            if color[1] == 'b' && num > 14
                return false
            end
            if color[1] == 'r' && num > 12
                return false
            end
            if color[1] == 'g' && num > 13
                return false
            end
        end
    end
    _, game_num = split(game, ' ')
    return parse(Int, game_num)
end


function fewest_cubes(line)
    game, rslt = split(line, ':')
    round = split(rslt, ';')
    red, green, blue = 0, 0, 0
    for hand in round
        x = split(hand, ',')
        for blocks in x
            _, num, color = split(blocks, ' ')
            num = parse(Int, num)
            
            if color[1] == 'b' 
                blue = max(num, blue)
            
            elseif color[1] == 'r' 
                red = max(num, red)
            
            elseif color[1] == 'g'
                green = max(num, green)
            
            else 
                println("ERROR INCORRECT COLOR")
            end
        end
    end
    return red*green*blue
end





function main()
    f = open("input_files/day_2.txt")
    lines = readlines(f)
    f_test = open("input_files/day_2_test.txt")
    lines_test = readlines(f_test)
    println(solver(lines_test, false))
    println(solver(lines, false))
    println(solver(lines_test, true))
    println(solver(lines, true))



end

main()