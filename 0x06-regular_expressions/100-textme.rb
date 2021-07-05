#!/usr/bin/env ruby

arr = ARGV[0].scan(/(?:from:(Google|\+?\d{11})|to:(.+?\d{10})|flags:(............1?))/)

for i in 0..arr.length-1
    if arr[i] != nil
        for j in 0..arr[i].length-1
            if arr[i][j] != nil
                print arr[i][j]
            end
        end
    end
    if i != arr.length-1
        print ','
    end
end
puts ""
