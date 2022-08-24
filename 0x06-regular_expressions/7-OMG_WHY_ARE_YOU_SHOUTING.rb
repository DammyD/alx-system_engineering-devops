#!/usr/bin/env ruby
# The regular expression that match only capital letters
puts ARGV[0].scan(/\p{Lu}/).join
