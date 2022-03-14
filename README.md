# Pi(e)
A recipe for a nice cake that approximates pi when compiled in Chef

A WYSIWILPDAFGBAIS (What you see is - well, it looks pretty dumb at first glance but actually it's smart) - tool

## Important note
This program won't compile correctly in a standard Chef-compiler, because the version of Chef that I used differs slightly from the [specification][1] - see below for an explanation. In an oven, however, it will compile correctly and produce a nice cake. Probably. No guarantee. For me it worked at least.

## What are those files?
- pi.chef: The source code for the Chef program that approximates pi and gives a nice cake. The program will prompt you for "fifty grams of butter", here you may enter any positive whole number you like. The bigger it is, the longer the program will take, but the better the approximation for pi will be, too.
- int.py: The interpreter. It uses Chef.py. Usage: ```py int.py <filename> [d]```, where "filename" is the path to the Chef source code, and the optional "d" enables debugging mode, which prints out some maybe useful information if you're developing a Chef program yourself. It is however not intended to be used by people other than me and thus it may not be clear what the information means.
- Chef.py: The core of the interpreter. Use by executing int.py as described above.

## How it works
The recipe is based on a recipe that was printed on some baking ingredient produced by cebe. It produces a very tasty cake.

The algorithm behind the program is really nice in my opinion. You take a square with sidelength l and cut it up evenly in lxl smaller squares (sidelength 1). Next, you count how many of those small squares have a distance less than l from one particular (e.g. the lower left) corner of the big square. You then divide this number by the total number of small squares. Doing this will give you the ratio of the area of a quarter circle around your selected corner with radius l to the area of the big square, or rather, an approximation to this ratio, because you can only approximate the circle with your small squares. But you can also compute that ratio: The square has area l^2, the quarter circle has area (pi\*l^2)/4, so the ratio will approximate pi/4. So multiplying your ratio by 4 will give you something close to pi. Increasing your l will also increase the quality of your approximation.

Now, implementing this algorithm in most other languages is fairly simple, you can do it in less than ten lines probably. In Chef, however, we have some problems: First of all, we don't have a square root operation built into the language, but we need to take a square root to get the distance of the small squares from the corner. We solve this by simply writing an algorithm into our program that does square roots. I used the [babylonian method](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method) for that.

The second problem however is much bigger. Let me start it this way: The [language specification of Chef][1] does not specify the types of numbers you may use in your variables a.k.a. ingredients. You have two options, either you only use integers (which would be a pain to use for something like computing pi, a non-integer, you basically would have to code your own system of handling floats, and good luck trying to convert the result into a usable recipe), so for example division would simply discard the remainder and produce only whole numbers, or you allow floats too, which brings another big problem: You can only branch in Chef by testing whether a number is zero or not. So to compare two positive integers you can simply subtract one of both of them repeatedly, and whichever number is smaller will hit zero first. With floats however you can't do that, the program has no way of telling whether a number is greater than zero, less than zero, or even compare it to another number. But in our algorithm above we need to compare the distance of the small square from the corner to the sidelength of the big square. So to solve this, I changed the meaning of the branching instruction in Chef to test for smaller or equal to zero instead of just equal to zero. For any program that uses only non-negative integers, the result should be the same as with any other compiler, so I count that as only a small, but very useful change in the language standard.

Another change to the language standard was made, but it is something almost every Chef interpreter does: The interpreter does not know about correct participles of verbs and basically simply puts an "ed" at the and of the verb, which leads to funny instructions such as "Proceed until doed" (instead of "Proceed until done"). This is simply due to the English language being far too complex to implement in a interpreter like that.

So with all that being said, we can finally move on to writing the code. If you want a detailed explanation of it, see extras/pi_explained.txt.

## Does it actually work?
The program does definetly work, although being relatively slow, at least for large values of "fifty grams of butter". The cake works too, although being really tideous to make, because you have to insert most of the ingredients in really small amounts really often, sometimes multiple times in a row. For some impressions of the process, look at extras/pie_making.md.

## Takeaways
Chef is not a good language.

As sad as this is, in my opinion it completely fails its main design principle: Producing usable recipes. I will give some examples:
1. Probably the worst of all: You can only change ingredients (a.k.a. variables) via the "Fold" instruction. Since you also cannot do arithmetics only with values in the mixing bowls, but have to store them into a variable and then add it back into the bowl, you need this instruction extremely often. The problem with that: Almost never in an actual recipe do you need to fold in an ingredient. This is no big problem in practice, you just put the ingredient into the mixing bowl and move on, but it just looks so dumb. And also using the same instruction over and over again could be so easily avoided by just implementing a way of doing arithmetic with the values in the mixing bowls directly, e.g. adding the two top values of the stack together, or things like duplicating the top value.
2. The instrucions are very incoherent about using articles, e.g. you have to use "Put (ingredient) into mixing bowl", but "Stir (ingredient) into _the_ mixing bowl". Again, this has no practical implications, but it just looks dumb.
3. Functions: It's almost heartbreaking how this cool feature is ruined. You can write and use functions fairly easy, and it's very nice. But how do you call a function? With the "Serve with" instruction! So to get a working recipe, you have to put this at the end of your recipe, because it makes no sense to serve the food before it is finished. And what sense do funtions make if put only at the end of the rest of your code? Again, this is so sad.
4. You can't do much after actually cooking the food, because it has to be in the baking dish at this point, and you can only interact with those dishes by pouring contents of mixing bowls into them. Also, there is no explicit "Bake the ..." instruction, so that in and of itself would be a problem.
5. There are no comments. This is very bad when developing, but also in the final recipe it would be nice to be able to have lines that don't actually do anything. You may have to prevent comments like "Don't actually execute the following instruction when cooking", but that would surely be possible with some thinking.

I could go on, but those are some reasons why I don't like Chef after the experience of writing this program.

Side note: This is not an attack on Chef's developer, David Morgan-Mar. After all, Chef is an esoteric language and probably a joke language, so I should not expect a good language. It is simply the factual statement: Chef is bad, at least in my opinion. And there's nothing wrong with that.
So in conclusion, I will probably never use Chef again.
But after all, the making of this project still was a fun experience.


Happy pi-day!


[1]: https://www.dangermouse.net/esoteric/chef.html
