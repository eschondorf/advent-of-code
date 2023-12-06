import DelimitedFiles

function solver(A, part2 = false)
    rv = 0
    m, _ = size(A)
    if ! part2
        B = find_partial_locs(A)
        j = 1
        while j <= m
            i = 1
            while i <= m
                #println((i, j))
                if B[i,j] == 1 && isdigit(A[i, j])
                    num, lb, ub = pick_out_num(A, i, j, m)
                    rv += num
                    i += ub 
                end
                i += 1
    
            end
            j+=1
        end
    end
    if part2
        for line in arr
            
        end
    end
   return rv
end

function pick_out_num(A, i, j, m)
    ub = -1
    lb = -1
    k = 0
    b1 = true
    b2 = true
    if i == 1
        lb = 0
    else
        while b1
            if i-k == 0 || !(47 < Int(A[i - k, j]) < 58)
                break
            end
            k += 1
        end
        lb = k-1
    end
    k = 0
    if  i == m
        ub = 0
    else
        while b1
            if i+k == m+1 || !(47 < Int(A[i + k, j]) < 58)
                break
            end
            k += 1
        end
        ub = k-1
    end
    return parse(Int,join(A[i-lb: i + ub, j])), lb, ub
end


function in_arr(k, m)
    if k > m
        return false
    elseif k < 1
        return false
    else
        return true
    end
end

function find_partial_locs(A)
    m, _ = size(A)
    partial_locs = zeros(Int, m, m)
    for j in 1:m
        for i in 1:m
            if !((47 < Int(A[i, j])< 58)|| (Int(A[i, j]) == 46))
                for l in -1:1
                    for k in -1:1
                        if (k!= 0 || l != 0)
                            if (in_arr(i +k, m) && in_arr(j+l, m))
                                partial_locs[i+k, j+l] = 1
                            end
                        end
                    end
                end
            end

        end
    end
    return partial_locs

end


function get_gears(A)
    rv = 0
    m, _ = size(A)
    for j in 1:m
        for i in 1:m
            if Int(A[i, j]) == 42
                test = zeros(Int, 3,3)
                vals = Set()
                neighbors = 0
                for l in -1:1
                    for k in -1:1
                        if (k!= 0 || l != 0)
                            if (in_arr(i +k, m) && in_arr(j+l, m))
                                if 47 < Int(A[i+k, j+l])< 58
                                    test[k+2, l+2] = 1
                                    num, _, _ = pick_out_num(A, i+k, j+l, m)
                                    push!(vals, num)
                                end
                            end
                        end
                    end
                end
                for k in 1:3
                    b_s = join(string.(test[:, k]))
                    dec = parse(Int, b_s, base=2)
                    if dec==0
                        neighbors += 0
                    elseif dec == 5
                        neighbors += 2
                    else
                        neighbors += 1
                    end
                end
                #println(test)
                #println(neighbors)
                temp = 1
                if neighbors == 2
                    if length(vals) == 1
                        for elt in vals
                            #println(140)
                            temp = elt^2
                            rv += elt^2
                        end
                    elseif length(vals) == 2
                        for elt in vals
                            temp = temp * elt
                        end
                        rv += temp
                        
                    else
                        error("ERROR MORE THAN THREE ELEMENTS IN SET")
                    end
                    #println(temp)
                    #println(rv)
                    
                end
                
            end

        end
    end
    return rv
    
end




function read_grid(file_path::AbstractString)
    # Open the file for reading
    file = open(file_path, "r")

    # Initialize an empty array to store the grid
    grid = []

    try
        # Read each line from the file
        for line in eachline(file)
            # Split the line into characters and append it to the grid
            push!(grid, [ch for ch in line])
        end
    finally
        # Close the file
        close(file)
    end

    # Convert the array of arrays to a 2D array (matrix)
    matrix = hcat(grid...)

    # Return the transpose of the matrix
    return matrix
end







function main()
    #f = open("input_files/day_2.txt")
    #arr = readlines(f)
    #f_test = open("input_files/day_2_test.txt")
    arr_test = read_grid("input_files/day_3_test.txt")
    arr = read_grid("input_files/day3.txt")
    ##println(solver(lines_test, false))
    ##println(solver(lines, false))
    ##println(solver(lines_test, true))
    ##println(solver(lines, true))
    ##println(solver(arr_test))
    ##println(solver(arr))
    println(get_gears(arr_test))
    println(get_gears(arr))


end

main()