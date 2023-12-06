function solver(arr, part2 = false)
    rv = 1
    if ! part2
        time, dist = parse_arr(arr)
        for i in 1:length(time)
            ub, lb = quad_eq(time[i], dist[i])
            rv *= (ub - lb+1)
        end
    end
    if part2
        time, dist = parse_arr(arr)
        new_time = parse(Int, join(string.(time)))
        new_dist = parse(Int, join(string.(dist)))
        ub, lb = quad_eq(new_time, new_dist)
        rv = Int(ub - lb+1)
    end
   return rv
end


function parse_arr(arr)
    time_str = arr[1]
    dist_str = arr[2]
    time_lst = split(split(time_str, ':')[2])
    time_lst_ints = [parse(Int, num) for num in time_lst]
    dist_lst = split(dist_str, ':')[2]
    dist_lst_ints = [parse(Int, num) for num in split(dist_lst)]
    return time_lst_ints, dist_lst_ints
end


function quad_eq(t, d)
    disc = sqrt(t^2 - 4*d)
    lb = floor((t - disc)/2 + 1)
    ub = ceil((t+disc)/2 - 1)
    return ub, lb

end



function main()
    f = open("input_files/day_6.txt")
    lines = readlines(f)
    f_test = open("input_files/day_6_test.txt")
    lines_test = readlines(f_test)
    println(solver(lines_test, false))
    println(solver(lines, false))
    println(solver(lines_test, true))
    println(solver(lines, true))



end

main()