# CTF-picoFlag
So currently my main focus is strengthening my knowledge of tech in general with the idea of getting into a Tech position.
My main focus at this time (Aug 23) is AWS, but I'm also trying to learn coding concurrently (Python) so that I have at least #the competency to write basic scripting when needed. Further, with an eye to the future and because how interdependent so many of these technologies are, I'm playing around with hacking via CTF to get more familiar with the tools and techniques to break systems. Any part of the technology chain being compromised can open up the entire system, so a holistic approach to responsible implementation of any of these technologies is necessary to provide even a modicum of security. This takes #at least a beyond surface level understanding of how each component of a system not only works but also interacts with other #systems.

Also, ctf presents me with a fairly constantly changing set of topics that is more fun than the deep dives elsewhere in my learning.

##My approach to ctf:

###Give the specific flag a fair shot
This means apply the tools I know how to use to the extent that I know how to use them, and leverage things like search engines to try to find out more about the givens in a scenario to see if I can figure out some way to exploit it.

###Bang Head against the wall a few times. Remind myself to always try the obvious first.
Not that I have a ton of skill to lean on to aim for elegant solutions every time, my ego pushes me to look for the elegant when in reality what I need to be doing is focusing on achieving the goal. There's some benefit to this drive for elegance (or cleverness in that it will have me engaging more deeply with whatever I'm dealing with, but the downside is that it can be extremely frustrating.

###Look up a writeup, shamelessly
The picoCTF scenario STONKS -- just looking over it, it jumped out to me that I had to send something to break the server to get a different response. For the life of me, I couldn't figure out what that actually was. I tried a bunch of strings and couldn't get it to do anything but spit back out a random list of stocks. I found a writeup that said it needed to be a string of %f repeated over and over again, but it didn't quite understand why that worked either. Because I was a bit frustrated by the process, I put the solution to use, then moved on, but I made a note of it to circle back to when I had a different frame of mind. I moved on to some other scenarios, then the next day dug in deeper to find that it was an "uncontrolled format string" vuln with the c function printf(). This allows you to use %n/%f type tokens to force the program to return values from spots in memory that aren't necessarily intended to be accessed in that way.

I'm also fairly quick to look up writeups that deal with tools/things I have next to no knowledge of. This is because they are typically fairly poorly written in terms of specific steps (as in a granular: Step A, Step B, Step C with each individual click/command detailed) while giving the general steps taken with that tool. This greatly reduces the learning curve of whatever by giving some direction, but still allows for a level of self-discovery and exploration that assists me at my current level with a concrete use case.
