#converting my armstrong calculator to ruby just to get a handle on how ruby works
#This code is effectively the same as the C++ armstrong program, refer to that to see the logic applied here
#As I really dont need to reiterate anything
calc = Array.new(4)
exponentialValue = Array.new(4)
puts "Input a number"
input = gets.to_i
checker = 100
armStrong = 1
numberBin = 0
counter = 1
while counter <= input
  counter += 1
	
	if armStrong == counter/checker
		checker = checker + 100
		#uncomment above just to see if checker is working correctly
		numberBin += 1
		#Uncomment above if you want to see if number bin is working
		end
end
#Line 26
calc[0] = numberBin
armStrong = numberBin * 100
input2 = input - armStrong
numberBin = 0
armStrong = 1
checker = 10
counter = 1
#Line 35
while counter < input2
	counter += 1
	
		if armStrong == counter/checker
			checker = checker + 10
			numberBin += 1
		end
end
#line 42
calc[1] = numberBin
armStrong = (calc[0] * 100) + (calc[1] * 10)
tenth = input - armStrong
calc[2] = tenth
exponentialValue[0] = calc[0]**3
exponentialValue[1] = calc[1]**3
exponentialValue[2] = calc[2]**3

sum = exponentialValue[0] + exponentialValue[1] + exponentialValue[2]

puts "your number is #{input} , the individual numbers cubed results in #{exponentialValue[0]}, #{exponentialValue[1]}, and #{exponentialValue[2]}"
puts "the resulting sum from the cube of the digits is #{sum}"
puts "Is this an armstrong number? : "
if sum == input
	puts "True"
else
	puts "False"
end
#Line 50
