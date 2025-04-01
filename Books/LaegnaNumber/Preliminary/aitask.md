
# AI task

- Use Python

1. Create mapping of Decimal System, where you have a special __str__ function despite otherwise it's a normal Integer
   - str function returns "U" if number is zero.
   - if it's above zero, it first adds 1, then digitvice reverses the digit value space: each number in each digit position x from 0-9 is replaced with y, which equals 9-x, so that 0 maps to 9, 1 maps to 8, -123 maps in whole integer to -987.
-- if it's a positive number, simply add 1 and do not reverse the digit mapping (I added this for the AI, the "don't" part).

   1. The resulting class behaves like an integer, much the way UserDict maps dictionaries, this class maps integers.

2. Create class using the decimal mapping class described in task 1, which would read a source of basic math lessons with positive and negative integers, for example "jane did buy 5 apples. how many apples does jane have now?" It will read all the integers into decimal mapping class instance, get their str value, and textually replace the str value; it would produce Markdown with all the lessons in anki-compatible format, and finally feed them to anki and produce new sets of lessons.
  - If not given, AI will autodownload some lessons from Hugging Face or Kaggle, ensuring the dataset is working and compatible with client's plans, for example how many, how big cards to have and in which format - Q&A, or Q&A&D, Question&Answer&Context or Document.

3. It would train the AI: download proper model from Hugging Face, fit.

4. It produces a gguf model compatible with Jan, GPT4All and LM Studio: thus, it's default model would be llama3.2:1b or qwen2.5:0.5b; if this takes hours or days and user is ready to spend more with their hardware capabilities: try Llama 3.2 1B Instruct or Qwen2-1.5B-Instruct; otherwise, if it's still fast, try CodeLlama-7b and CodeLlama-13b and try to integrate them into Code Assistant, if user needs to do something with our Markdown Document structure with VSCode, to help them with Laegna-aware bot. You can train GPT-2 or GPT-3, which is a more serious work and would enable intelligence on Laegna theory: you can repeat most of the basic math there and explain the meanings in symmetries of it's letter sequences.

Second Part
-----------

Write this class:
- It emulates Integer, based on the last class implemented (in any other relation than __str__ string output, already breaking some clients, they would do normal math).
- When user is doing subsequently the basic operations of math:
  - If they are adding and subtracting, the hidden parameter would change as much as they would need to muliply or divide, to get the same result, in relative size symmetries of subsequent numbers being operated.
  - If they are multiplying and dividing, it creates the subsequent fix to plus-minus counter, another hidden memory, which contains how much would be second number bigger than first when using adding, and thereby the plus-minus numbers would not lose their _proportions_.
  - As both operators are now symmetric, as they are open and describe their doings to others by providing them R number in addition to T (you can show number and fix, digitwise mixed, in RTRTRTRT.RTRTRTRT digit format).

Third Part
----------

If you are still unhappy, you can implement floating point numbers (not only whole, positive naturals), exclamation mark to take limit value, and more laegna behaviors to more decimal formats, operations and conditions.