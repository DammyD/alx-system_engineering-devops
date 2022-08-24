#!/usr/bin/env ruby
# The regular expression that match a string with h and n
puts ARGV[0].scan(/^h.n$/).join
