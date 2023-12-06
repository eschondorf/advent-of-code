function solver(f_name, part2 = false)
    rv = 0
    seeds, seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc = parse_text_file(f_name)
    dicts = [seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]
    if part2
        new_seeds = []
        for i in 1:2:length(seeds)
            println(i)
            rang = seeds[i+1]
            old_seed = seeds[i]
            println(rang)
            for j in 1:rang
                append!(new_seeds, old_seed + j - 1)
            end
        end
        seeds = new_seeds
    end

    old = seeds
    i = 1
    for elt in dicts
        print(i)
        new = []
        for val in old
            append!(new, get_next_val(val, elt))
        end
        #println(new)
        old = new
        i +=1
    end
    return minimum(old)
            

    
end


function part_2_brute(f_name)
    t = time()
    seeds, seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc = parse_text_file(f_name)
    dicts = [seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]
    in_range = false
    i = 0
    while !in_range
        #println(i)
        val = map_backwards(i, dicts)
        if in_seed_range(seeds, val)
            return i, time() - t
        end
        i += 1
        if i > 10^(20)
            break
        end
    end
        


end

function in_seed_range(seeds, val)
    for i in 1:2:length(seeds)
        rang = seeds[i+1]
        old_seed = seeds[i]
        if old_seed <= val < old_seed + rang
            return true
        end
    end
    return false
    
end

function map_backwards(x, dicts)
    for d in reverse(dicts)
        x = get_next_val_rev(x, d)
    end
    return x

end


function get_next_val_rev(x, lst)
    for elt in lst
        dest, source, range = elt
        if dest <= x < dest + range
            #println(x)
            #println(source)
            return source + x - dest 
        end
    end
    return x
end


function solver_pt_2(f_name)
    seeds, seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc = parse_text_file(f_name)
    dicts = [seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]
    seed_ranges ==[(seeds[i], seeds[i+1]) for i in 1:2:length(seeds)-1]
    old_ranges = seed_ranges
    i = 1
    for elt in dicts
        new = []
        for val in old
            append!(new, get_next_val(val, elt))
        end
        #println(new)
        old = new
        i +=1
    end
    return minimum(old)

    
end



function get_next_range(ran, lst)
    val, l = ran
    rv = []
    for elt in lst
        dest, source, range = elt
        if source <= x < source + range
            #println(x)
            #println(source)
            if l <= range
                return [[dest + x - source, l]]
            else
                append!(rv, [dest + x - source, range])
                rv += get_next_range([x+range, l-range], lst)
            end


            return dest + x - source 
        end
    end
    return x
end


function parse_text_file(file_path::AbstractString)
    try
        # Read the entire content of the file
        content = read(file_path, String)
        
        # Split the content based on two consecutive newline characters
        sections = split(content, r"\n\n")

        seeds = [parse(Int, b) for b in split(split(sections[1], ':')[2])]
        seeds_soil = [[parse(Int, x) for x in split(b)] for b in split(split(sections[2], ':')[2], '\n')[2:end]]
        soil_fert = [[parse(Int, x) for x in split(b)] for b in split(split(sections[3], ':')[2], '\n')[2:end]]
        fert_water = [[parse(Int, x) for x in split(b)] for b in split(split(sections[4], ':')[2], '\n')[2:end]]
        water_light = [[parse(Int, x) for x in split(b)] for b in split(split(sections[5], ':')[2], '\n')[2:end]]
        light_temp = [[parse(Int, x) for x in split(b)] for b in split(split(sections[6], ':')[2], '\n')[2:end]]
        temp_humid = [[parse(Int, x) for x in split(b)] for b in split(split(sections[7], ':')[2], '\n')[2:end]]
        humid_loc  = [[parse(Int, x) for x in split(b)] for b in split(split(sections[8], ':')[2], '\n')[2:end]]

        return seeds, seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc
    catch e
        println("Error reading or parsing the file: $e")
        return []
    end
end


function get_next_val(x, lst)
    for elt in lst
        dest, source, range = elt
        if source <= x < source + range
            #println(x)
            #println(source)
            return dest + x - source 
        end
    end
    return x
end



function main()
    #f = read("input_files/day_5.txt")
    #lines = readlines(f)
    #f_test = read("input_files/day_5_test.txt")
    #lines_test = readlines(f_test)
    #println(solver("input_files/day_5_test.txt", false))
    #println(solver("input_files/day_5.txt", false))
    println(part_2_brute("input_files/day_5_test.txt"))
    println(part_2_brute("input_files/day_5.txt"))
    #println(parse_text_file("input_files/day_5_test.txt"))
    
    #=
    seeds, seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc = parse_text_file("input_files/day_5_test.txt")
    dicts = [seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]
    println(map_backwards(86, dicts))
    =#
    


end

main()