#!/usr/bin/env ruby
# The regular expression that match a string that starts with h and ends with n
puts ARGV[0].scan(/^h.n$/).join
