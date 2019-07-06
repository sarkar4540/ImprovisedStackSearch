# Introduction

Improvised Stack Search is an application designed primarily to
search the [StackOverflow](http://stackoverflow.com) site using a 
query and obtain a specific number of relevant questions, and their 
most relevant answer. The application is written in Python and is
designed to run on various Cloud Platforms with minimum changes.

# Usage

## Obtaining Sources

```bash
git clone https://github.com/sarkar4540/ImprovisedStackSearch.git
cd ImprovisedStackSearch
```
## Running as Script

```bash
python run.py
```
#### Output:
```
Enter the search string:How to read XTrace files using java and get method trace
Enter number of answers(max 50):10
Extracted tags: ['xtrace', 'files', 'java', 'method', 'trace']
Got 100 questions... processing.
Ranking questions... 
Done.
Fetching and ranking answers based on comments...
Done.
Picking top answers for questions...
Done.
[{"index": 0, "question": {"tags": ["java"], "owner": {"reputation": 8, "user_id": 7101345, "user_type": "registered", "profile_image": "https://www.gravatar.com/avatar/b52d1b11f373e8bf17f3ef6a29747a92?s=128&d=identicon&r=PG&f=1", "display_name": "sdfjbs", "link": "https://stackoverflow.com/users/7101345/sdfjbs"}, "is_answered": true, "view_count": 219, "closed_date": 1506357185, "accepted_answer_id": 46409586, "answer_count": 4, "score": -6, "last_activity_date": 1506356725, "creation_date": 1506354792, "last_edit_date": 1506354997, "question_id": 46409350, "link": "https://stackoverflow.com/questions/46409350/method-to-find-and-search-files-java", "closed_reason": "off-topic", "title": "method to find and search files JAVA", "body": "<p>I need help with a method that finds a specific file and then prints out a line of text from that file. The line of text is printed if the string typed in the console matches a string from that line of text. For example if I were to call <code>java Find ring report.txt address.txt Homework.java</code> it should print something like:</p>\n\n<p><code>report.txt: has broken up an internationa ring of DVD bootleggers that</code> </p>\n\n<p><code>address.txt: Kris Kringle, North Pole</code> </p>\n\n<p><code>address.txt: Homer Simpson, Springfield</code> </p>\n\n<p><code>Homework.java: String file name;</code>    </p>\n\n<p>The specified word is always the first command line argument.</p>\n\n<p>This is what I have so far:</p>\n\n<pre><code>import java.io.File;\nimport java.io.FileNotFoundException;\nimport java.util.Scanner;\n\n\n/**\n * Code for E11.8. Searches all files specified on the command line and prints out all lines     \n  containing a specified word.\n * @Michael Goedken\n */\npublic class Find\n{\n   /**\n      Searches file for a word, prints out all lines containing that word.\n      @param wordToFind the word to find\n      @param filename the filename for the file to search\n   */\n   public static void findAndPrint(String wordToFind, String filename)\n   {\n   String input = args[0];\n   for (int i = 1; i &lt; args.length; i++)\n   {\n       System.out.println(\" File  \" + args[i]);\n        File one = new File(args[i]);\n        Scanner in = new Scanner(one);\n\n        while (in.hasNext())\n       {\n           String line = in.nextLine();\n            if (line.contains(input))\n            {\n               System.out.println(line);\n            }\n       }\n   }\n\n\n}\n\n   /**\n      First argument of the main method should be the word to be searched\n      For other arguments of the main method, store the file names to be examined\n   */\npublic static void main(String[] args)\n{\n   // call findAndPrint for each text file\n\n\n\n   }\n }\n</code></pre>\n", "answer_scores": {"46409833": 0, "46409786": 0.0, "46409902": 0, "46409586": -0.72003}}, "answer": {"owner": {"reputation": 1238, "user_id": 6554747, "user_type": "registered", "accept_rate": 100, "profile_image": "https://i.stack.imgur.com/Xlzqs.png?s=128&g=1", "display_name": "progyammer", "link": "https://stackoverflow.com/users/6554747/progyammer"}, "is_accepted": false, "score": 1, "last_activity_date": 1506356494, "creation_date": 1506356494, "answer_id": 46409833, "question_id": 46409350, "body": "<p>You're trying to access the array <code>args[]</code> which is not in the scope of the function <code>findAndPrint()</code>. You need to pass <code>args[0]</code> as an argument to the function call statement in the main method:  </p>\n\n<pre><code>public static void main(String[] args){\n    findAndPrint(args[0], args[1]); //for report.txt\n    findAndPrint(args[0], args[2]); //for address.txt\n}\n</code></pre>\n\n<p><code>args</code> is an argument of the main method. It is a String array that stores the individual command line inputs. In your case, the contents of the array <code>args[]</code> are = <code>{\"ring\", \"reports.txt\", \"address.txt\", \"Homework.java\"}</code>.  </p>\n\n<p>You can modify your <code>findAndPrint()</code> function in this way now:  </p>\n\n<pre><code>static void findAndPrint(String wordToFind, String filename){\n    Scanner fscan = new Scanner(new File(filename));\n    String str = \"\";\n    while((str = fscan.nextLine()) != null){\n        if(str.contains(wordToFind))\n            System.out.println(str);\n    }\n}\n</code></pre>\n"}}, {"index": 1, "question": {"tags": ["java", "trace"], "owner": {"reputation": 11, "user_id": 6350335, "user_type": "registered", "profile_image": "https://lh4.googleusercontent.com/-B8xzQ3XK2DQ/AAAAAAAAAAI/AAAAAAAAPnI/AzQJIZVwNQ0/photo.jpg?sz=128", "display_name": "Susheel Rao", "link": "https://stackoverflow.com/users/6350335/susheel-rao"}, "is_answered": true, "view_count": 25, "accepted_answer_id": 56008887, "answer_count": 1, "score": -1, "last_activity_date": 1557159171, "creation_date": 1557158921, "question_id": 56008818, "link": "https://stackoverflow.com/questions/56008818/how-to-trace-a-java-flow-from-method-to-method-using-java", "title": "How to Trace a Java flow from Method to method using Java", "body": "<p>I want to trace a Java flow whenever there is a Exception happening . I mean Like Consider</p>\n\n<p>Method1 -> Method2 -> Method3 -> Method4 -> Error Came in Method 4 while processing argument1, let\u2019s say we find it invalid.</p>\n\n<p>Then, we could have a response element which looks like below:</p>\n\n<p>\u201cDebugInfo\u201d : \u201cMethod1|Method2|Method3|Method4 - Error Came in Method 4 while processing argument1. It is invalid because destination does not support HAL\u201d</p>\n", "answer_scores": {"56008887": 0.771459}}, "answer": {"owner": {"reputation": 20210, "user_id": 1803853, "user_type": "registered", "accept_rate": 71, "profile_image": "https://www.gravatar.com/avatar/af9689064b2f7b82d2147bbf7f10d4d7?s=128&d=identicon&r=PG", "display_name": "Davide Lorenzo MARINO", "link": "https://stackoverflow.com/users/1803853/davide-lorenzo-marino"}, "is_accepted": true, "score": 2, "last_activity_date": 1557159171, "creation_date": 1557159171, "answer_id": 56008887, "question_id": 56008818, "body": "<p>This is exactly what happens using the method <a href=\"https://docs.oracle.com/javase/7/docs/api/java/lang/Throwable.html#getStackTrace()\" rel=\"nofollow noreferrer\">getStackTrace</a>:</p>\n\n<blockquote>\n  <p>Provides programmatic access to the stack trace information printed by printStackTrace(). Returns an array of stack trace elements, each representing one stack frame. <strong>The zeroth element of the array</strong> (assuming the array's length is non-zero) <strong>represents the top of the stack, which is the last method invocation in the sequence</strong>. Typically, this is the point at which this throwable was created and thrown. The last element of the array (assuming the array's length is non-zero) represents the bottom of the stack, which is the first method invocation in the sequence.</p>\n</blockquote>\n\n<p>Note that the order is exactly the opposite as you need (see the bold part)</p>\n\n<p>So you can do something like</p>\n\n<pre><code>StackTraceElement[] elements = exception.getStackTrace();\nfor (int i = elements.length() - 1; i &gt;= 0; i--) {\n   System.out.println(elements[i].getMethodName());\n}\n</code></pre>\n\n<p>You need only to add some templating to that to get exactly what you need.</p>\n\n<p>Note that printing (or exporting) only the method name is not enough because generally you have a stack moving through different classes so it is better to print class name and method name. But for larger methods is useful also to know at which row it happened, so... why don't use a simple <code>exception.printStackTrace()</code> that does exactly what you need?</p>\n"}}, {"index": 2, "question": {"tags": ["groovy"], "owner": {"reputation": 3202, "user_id": 271599, "user_type": "registered", "accept_rate": 57, "profile_image": "https://www.gravatar.com/avatar/de267f213b375efca5da07890e5efc25?s=128&d=identicon&r=PG", "display_name": "dromodel", "link": "https://stackoverflow.com/users/271599/dromodel"}, "is_answered": true, "view_count": 18185, "accepted_answer_id": 6259292, "answer_count": 2, "score": 17, "last_activity_date": 1524735965, "creation_date": 1307403255, "question_id": 6259202, "link": "https://stackoverflow.com/questions/6259202/how-do-i-print-a-groovy-stack-trace", "title": "How do I print a Groovy stack trace?", "body": "<p>How do I print a Groovy stack trace? The Java method, Thread.currentThread().getStackTrace() produces a huge stack trace, including a lot of the Groovy internals. I'm seeing a function called twice from a StreamingMarkupBuilder that looks like it should only be called once and I would like to see why Groovy thinks it should be calling it twice.</p>\n", "answer_scores": {"6259292": -0.25721333333333335, "50039831": 0}}, "answer": {"owner": {"reputation": 7513, "user_id": 924597, "user_type": "registered", "accept_rate": 79, "profile_image": "https://i.stack.imgur.com/V1jPU.jpg?s=128&g=1", "display_name": "Shorn", "link": "https://stackoverflow.com/users/924597/shorn"}, "is_accepted": false, "score": 1, "last_activity_date": 1524735965, "creation_date": 1524735965, "answer_id": 50039831, "question_id": 6259202, "body": "<p>I found this questions when searching for <code>\"spock print full stack trace\"</code>.</p>\n\n<p>My unit tests are written in Groovy, using the Spock testing framework and they're run in the context of a Gradle build.</p>\n\n<p>The fix for me was as simple as adding <code>exceptionFormat = 'full'</code> to my Gradle test task specification: </p>\n\n<pre><code>test {\n  testLogging {\n    exceptionFormat = 'full'\n  }\n}\n</code></pre>\n"}}, {"index": 3, "question": {"tags": ["java", "methods", "call", "trace"], "owner": {"reputation": 61, "user_id": 4736373, "user_type": "registered", "accept_rate": 40, "profile_image": "https://www.gravatar.com/avatar/88a7a2c8f893c5d458caaf4c1b85f543?s=128&d=identicon&r=PG&f=1", "display_name": "george24", "link": "https://stackoverflow.com/users/4736373/george24"}, "is_answered": true, "view_count": 17870, "accepted_answer_id": 29384646, "answer_count": 2, "score": 8, "last_activity_date": 1532650310, "creation_date": 1427857849, "last_edit_date": 1427860073, "question_id": 29382231, "link": "https://stackoverflow.com/questions/29382231/how-do-i-trace-methods-calls-in-java", "title": "How do I trace methods calls in Java?", "body": "<p>Consider the two simple Java classes below:</p>\n\n<p><strong>First Example</strong></p>\n\n<pre><code>class Computer {\n    Computer() {\n        System.out.println(\"Constructor of Computer class.\");\n    }\n    void On() {\n        System.out.println(\"PC turning on...\");\n    }\n    void working() {\n        System.out.println(\"PC working...\");\n    }\n    void Off() {\n        System.out.println(\"PC shuting down...\");\n    }\n    public static void main(String[] args) {\n        Computer my = new Computer();\n        Laptop your = new Laptop();\n        my.On();\n        my.working();\n        your.On();\n        your.working();\n        my.Off();\n        your.Off();\n   }\n}\n</code></pre>\n\n<p><strong>Second Example</strong></p>\n\n<pre><code>class Laptop {\n    Laptop() {\n        System.out.println(\"Constructor of Laptop class.\");\n    }\n    void On() {\n        System.out.println(\"Laptop turning on...\");\n    }\n    void working() {\n        System.out.println(\"Laptop working...\");\n    }\n    void Off() {\n        System.out.println(\"Laptop shuting down...\");\n    }\n}\n</code></pre>\n\n<p>After the program run, how do I trace (1) which object call which method (2) and how many times?</p>\n\n<p>Just a little precision, I might have 100 classes and 1000s of objects each of them calling 100s of methods. I want to be able to trace (after I run the program), which object called which method and how many times.</p>\n\n<p>Thanks for any suggestion.</p>\n", "answer_scores": {"29384646": -0.32081133333333334, "51124195": 0}}, "answer": {"owner": {"reputation": 24121, "user_id": 173149, "user_type": "registered", "accept_rate": 62, "profile_image": "https://www.gravatar.com/avatar/e43539b3257049bef7885c9f193b364d?s=128&d=identicon&r=PG", "display_name": "gavenkoa", "link": "https://stackoverflow.com/users/173149/gavenkoa"}, "is_accepted": false, "score": 1, "last_activity_date": 1530455396, "creation_date": 1530455396, "answer_id": 51124195, "question_id": 29382231, "body": "<pre><code>$ jdb -classpath ... -sourcepath ... my.App\njdb&gt; stop on my.App.main\njdb&gt; run\njdb&gt; step          &lt;... repeat until get to interesting line...&gt;\njdb&gt; threads\njdb&gt; trace go methods 0x1    &lt;... 0x1 is our main thread ID ...&gt;    \njdb&gt; step\n                   &lt;...HERE you get full methods calls trace...&gt;\njdb&gt; quit\n</code></pre>\n"}}, {"index": 4, "question": {"tags": ["java", "xml", "xsd"], "owner": {"reputation": 307, "user_id": 753707, "user_type": "registered", "accept_rate": 70, "profile_image": "https://www.gravatar.com/avatar/b66e1d7efe9b5c15982928163d72e3e7?s=128&d=identicon&r=PG", "display_name": "DUFF", "link": "https://stackoverflow.com/users/753707/duff"}, "is_answered": true, "view_count": 969, "accepted_answer_id": 7941431, "answer_count": 3, "score": 5, "last_activity_date": 1513320306, "creation_date": 1319914106, "last_edit_date": 1513320306, "question_id": 7940931, "link": "https://stackoverflow.com/questions/7940931/java-methods-for-interrogating-xsd-files", "title": "Java methods for interrogating XSD files", "body": "<p>I have a set of xsd files for different data types. In the Java world, what is the best way to generate a list of the properties of the types?</p>\n\n<p>e.g. with these two files.</p>\n\n<p><strong>file: customer.xsd</strong></p>\n\n<pre><code>&lt;?xml version=\"1.0\" encoding=\"ISO-8859-1\" ?&gt;\n&lt;xs:schema xmlns:xs=\"http://www.w3.org/2001/XMLSchema\"&gt;\n&lt;xs:element name=\"customer\"&gt;\n  &lt;xs:complexType&gt;\n    &lt;xs:sequence&gt;\n      &lt;xs:element name=\"number\" type=\"xs:integer\"/&gt;\n      &lt;xs:element name=\"name\" type=\"xs:string\"/&gt;\n      &lt;xs:element name=\"address\" type=\"xs:string\"/&gt;\n    &lt;/xs:sequence&gt;\n  &lt;/xs:complexType&gt;\n&lt;/xs:element&gt;\n&lt;/xs:schema&gt;\n</code></pre>\n\n<p><strong>file: order.xsd</strong></p>\n\n<pre><code>&lt;?xml version=\"1.0\" encoding=\"ISO-8859-1\" ?&gt;\n&lt;xs:schema xmlns:xs=\"http://www.w3.org/2001/XMLSchema\"&gt;\n&lt;xs:element name=\"customer\"&gt;\n  &lt;xs:complexType&gt;\n    &lt;xs:sequence&gt;\n      &lt;xs:element name=\"orderid\" type=\"xs:integer\"/&gt;\n      &lt;xs:element name=\"customer\" type=\"xs:string\"/&gt;\n    &lt;/xs:sequence&gt;\n  &lt;/xs:complexType&gt;\n&lt;/xs:element&gt;\n&lt;/xs:schema&gt;\n</code></pre>\n\n<p>I'd like to do two things</p>\n\n<p><strong><em>1.</em></strong> a Java application which reads in the XSD and processes then (somehow?). So when you run the program it can print the properties out</p>\n\n<pre><code>&gt; java -jar printtypes.jar -f customer.xsd\n&gt; number : Integer\n&gt; name : String\n&gt; address : String\n</code></pre>\n\n<p><strong><em>2.</em></strong> some kind of transformation which generates a new file</p>\n\n<p>file: customer.properties</p>\n\n<pre><code>&lt;propertylist&gt;\n&lt;prop&gt;\n &lt;name&gt; orderid &lt;/name&gt;\n &lt;type&gt; integer &lt;/type&gt;\n&lt;/prop&gt;\n&lt;prop&gt;\n &lt;name&gt; customer &lt;/name&gt;\n &lt;type&gt; string&lt;/type&gt;\n&lt;/prop&gt;\n&lt;/propertylist&gt;\n</code></pre>\n\n<p>I tried to implement the program in (1) above using java reflection to interrogate Java classes generated by JAXB.\nThis created an instance of the class and interrogated the values and fields, but it does not work where values are composed of a sequence that is empty. There is no way to get back to the original type of the value due to type erasure. You end up with an empty ArrayList of something, but you don't know what.</p>\n\n<p>I'm from the C++ work so I'm a bit lost with all this Java technology at the moment. My Google powers have failed me - most of the JAVA/XSD posts I've seen talk about validation which is not what I want to do.</p>\n", "answer_scores": {"7941031": -0.11731175, "7941431": 0.026122000000000006, "7947681": 0}}, "answer": {"owner": {"reputation": 10973, "user_id": 359035, "user_type": "registered", "accept_rate": 92, "profile_image": "https://www.gravatar.com/avatar/69739f977d9a83ffb1bbdbe236a44680?s=128&d=identicon&r=PG", "display_name": "Bill", "link": "https://stackoverflow.com/users/359035/bill"}, "is_accepted": true, "score": 2, "last_activity_date": 1319919586, "creation_date": 1319919586, "answer_id": 7941431, "question_id": 7940931, "body": "<p>You might want to look into XSOM, its a project that will ingest your XML schema and produce objects that you can traverse and produce your desired results. </p>\n\n<p><a href=\"http://xsom.java.net/userguide.html\" rel=\"nofollow\">http://xsom.java.net/userguide.html</a></p>\n\n<p>Parsing schema by hand can be really tricky because there can be different ways to say basically the same thing.</p>\n"}}, {"index": 5, "question": {"tags": ["java", "jsp", "scriptlet"], "owner": {"reputation": 8565, "user_id": 95914, "user_type": "registered", "accept_rate": 87, "profile_image": "https://www.gravatar.com/avatar/043703d9aa973023306d6562404804b7?s=128&d=identicon&r=PG", "display_name": "chmoelders", "link": "https://stackoverflow.com/users/95914/chmoelders"}, "is_answered": true, "view_count": 269321, "protected_date": 1310383056, "accepted_answer_id": 3180202, "answer_count": 30, "score": 1612, "last_activity_date": 1547611068, "creation_date": 1278314646, "last_edit_date": 1440778660, "question_id": 3177733, "link": "https://stackoverflow.com/questions/3177733/how-to-avoid-java-code-in-jsp-files", "title": "How to avoid Java code in JSP files?", "body": "<p>I'm new to Java EE and I know that something like the following three lines</p>\n\n<pre><code>&lt;%= x+1 %&gt;\n&lt;%= request.getParameter(\"name\") %&gt;\n&lt;%! counter++; %&gt;\n</code></pre>\n\n<p>is an old school way of coding and in JSP version 2 there exists a method to avoid Java code in JSP files. Can someone please tell me the alternative JSP 2 lines, and what this technique is called?</p>\n", "answer_scores": {"3180202": 0.08119653333333332, "7059994": 0.15093399999999998, "3177761": 0.0, "3177764": 0.2687015, "3178138": 0, "5395987": 0, "4897057": 0, "3178032": 0.7039345, "7098720": 0.666689, "10555449": 0, "6077376": 0, "6670578": 0.3101075, "5087629": 0, "14539925": 0, "6240988": 0, "6646745": 0, "14442545": 0.0, "10681343": 0.43406733333333336, "17780850": 0, "22427102": 0, "17105374": 0, "9977740": 0, "34452329": 0.563571, "47577565": 0, "47780407": 0, "50949855": 0, "36576959": 0, "44979085": 0, "53572611": 0, "38388675": 0}}, "answer": {"owner": {"reputation": 58639, "user_id": 53897, "user_type": "registered", "accept_rate": 56, "profile_image": "https://www.gravatar.com/avatar/2e71c1745ebc5401c8c8dfbf7c9a5d30?s=128&d=identicon&r=PG", "display_name": "Thorbj&#248;rn Ravn Andersen", "link": "https://stackoverflow.com/users/53897/thorbj%c3%b8rn-ravn-andersen"}, "is_accepted": false, "score": 27, "last_activity_date": 1278318606, "creation_date": 1278318606, "answer_id": 3178032, "question_id": 3177733, "body": "<p>Experience has shown that JSP's have some shortcomings, one of them being hard to avoid mixing markup with actual code.</p>\n\n<p>If you can, then consider using a specialized technology for what you need to do.  In Java EE 6 there is JSF 2.0, which provides a lot of nice features including gluing Java beans together with JSF pages through the <code>#{bean.method(argument)}</code> approach.</p>\n"}}, {"index": 6, "question": {"tags": ["java", "concurrency"], "owner": {"reputation": 8, "user_id": 7021512, "user_type": "registered", "profile_image": "https://www.gravatar.com/avatar/41c5fd6a3b64a9622eedfe60d22f9107?s=128&d=identicon&r=PG&f=1", "display_name": "Kevin L&#243;pez", "link": "https://stackoverflow.com/users/7021512/kevin-l%c3%b3pez"}, "is_answered": true, "view_count": 51, "accepted_answer_id": 43167400, "answer_count": 1, "score": 1, "last_activity_date": 1491129902, "creation_date": 1491127484, "question_id": 43167079, "link": "https://stackoverflow.com/questions/43167079/why-this-concurrent-execution-always-give-me-the-same-trace", "title": "Why this concurrent execution always give me the same trace?", "body": "<p>I'm trying to understand concurrent execution in Java, but given this code :</p>\n\n<pre><code>class Inter extends Thread {\n    public void run() { \n        System.out.println(\"Starting...\"); \n        try {\n            sleep(10000);\n        } catch (InterruptedException e) {\n            System.out.println(\"Interrupted.\"); }\n        System.out.println(\"Finished.\"); \n    }\n\n    public static void main(String[] args) {\n        Inter hi = new Inter();\n        hi.start();\n        System.out.println(\"Sending interruption...\"); \n        hi.interrupt();\n        System.out.println(\"Sent.\"); \n    }\n}\n</code></pre>\n\n<p>I don't know why always give me this trace :</p>\n\n<pre><code>Sending interruption...\nSent.\nStarting...\nInterrupted.\nFinished.\n</code></pre>\n\n<p>No matter how many times I run :</p>\n\n<pre><code>$ java Inter\n</code></pre>\n\n<p>As fars as I know in Java, when we execute the start() method in a new thread, the execution of this thread starts.</p>\n\n<p>So , since the main thread and the Inter thread are concurrently executed, why can't be this a possible trace, ?</p>\n\n<pre><code>Starting..\nSending interruption..\nSent\nInterrupted\nFinished\n</code></pre>\n", "answer_scores": {"43167400": 0}}, "answer": {"owner": {"reputation": 3259, "user_id": 2657100, "user_type": "registered", "profile_image": "https://www.gravatar.com/avatar/d998dcf9d454b9d9349b29f84947f2da?s=128&d=identicon&r=PG", "display_name": "nandsito", "link": "https://stackoverflow.com/users/2657100/nandsito"}, "is_accepted": true, "score": 1, "last_activity_date": 1491129902, "creation_date": 1491129902, "answer_id": 43167400, "question_id": 43167079, "body": "<blockquote>\n  <p>So, since the main thread and the Inter thread are concurrently executed, why can't be this a possible trace?</p>\n</blockquote>\n\n<p>Yes, it can. If you run your program a thousand times, most probably you will have that output at least once.</p>\n\n<p>It's up to the operating system thread scheduler to arrange the threads execution in order to give that possible output, but we have no control over the scheduler. Hence, the importance of properly designing your code to prevent race conditions.</p>\n"}}, {"index": 7, "question": {"tags": ["java", "class", "reflection", "dynamic", "load"], "owner": {"reputation": 6652, "user_id": 771665, "user_type": "registered", "accept_rate": 84, "profile_image": "https://www.gravatar.com/avatar/71767e0ed49d1f8accdee17c5abf4474?s=128&d=identicon&r=PG&f=1", "display_name": "MirroredFate", "link": "https://stackoverflow.com/users/771665/mirroredfate"}, "is_answered": true, "view_count": 62139, "accepted_answer_id": 6219855, "answer_count": 3, "score": 40, "last_activity_date": 1546343784, "creation_date": 1307045595, "last_edit_date": 1442078221, "question_id": 6219829, "link": "https://stackoverflow.com/questions/6219829/method-to-dynamically-load-java-class-files", "title": "Method to dynamically load java class files", "body": "<p>What would be a good way to dynamically load java class files so that a program compiled into a jar can read all the class files in a directory and use them, and how can one write the files so that they have the necessary package name in relation to the jar?</p>\n", "answer_scores": {"6219855": -0.17431483333333334, "10067805": 0, "6219945": 0}}, "answer": {"owner": {"reputation": 547, "user_id": 1319039, "user_type": "registered", "profile_image": "https://www.gravatar.com/avatar/092ef386274cbf4c780e207c554ad7f5?s=128&d=identicon&r=PG", "display_name": "d2k2", "link": "https://stackoverflow.com/users/1319039/d2k2"}, "is_accepted": false, "score": 8, "last_activity_date": 1342614058, "last_edit_date": 1342614058, "creation_date": 1333932547, "answer_id": 10067805, "question_id": 6219829, "body": "<pre><code>MyClass obj = (MyClass) ClassLoader.getSystemClassLoader().loadClass(\"test.MyClass\").newInstance();\nobj.testmethod();\n</code></pre>\n\n<p>or</p>\n\n<pre><code>MyClass obj = (MyClass) Class.forName(\"test.MyClass\").newInstance();\nobj.testmethod();\n</code></pre>\n"}}, {"index": 8, "question": {"tags": ["spring", "http", "jetty", "trace", "embedded-jetty"], "owner": {"reputation": 23, "user_id": 4730012, "user_type": "registered", "profile_image": "https://www.gravatar.com/avatar/e56369a1200fc0e99d653af9f604c250?s=128&d=identicon&r=PG&f=1", "display_name": "Michal N.", "link": "https://stackoverflow.com/users/4730012/michal-n"}, "is_answered": true, "view_count": 7202, "accepted_answer_id": 29361924, "answer_count": 5, "score": 4, "last_activity_date": 1481013109, "creation_date": 1427724369, "last_edit_date": 1427734623, "question_id": 29348328, "link": "https://stackoverflow.com/questions/29348328/java-embedded-jetty-is-accepting-http-trace-method", "title": "Java embedded jetty is accepting HTTP TRACE method", "body": "<p>I'm trying to disable HTTP TRACE method in embedded Jetty. In Jetty doc's is info that HTTP trace is disabled by default, but for embedded it is still enabled. I was trying to disable trace as a security constraint as is done in jetty.xml.</p>\n\n<pre><code>    ServletContextHandler servletHandler = new ServletContextHandler(ServletContextHandler.SESSIONS | ServletContextHandler.SECURITY);\n    servletHandler.setClassLoader(Server.class.getClassLoader());\n    servletHandler.setContextPath(\"/\");\n    servletHandler.addEventListener(new ContextLoaderListener());\n    servletHandler.addServlet(new ServletHolder(new CXFServlet()), \"/*\");\n    servletHandler.setInitParameter(\"contextClass\", AnnotationConfigWebApplicationContext.class.getName());\n    servletHandler.setInitParameter(\"contextConfigLocation\", BeansConfig.class.getName());\n    servletHandler.setInitParameter(\"javax.ws.rs.Application\", DispatcherConfig.class.getName());\n\n     /*\n     * &lt;security-constraint&gt;\n     * &lt;web-resource-collection&gt;\n     * &lt;web-resource-name&gt;Disable TRACE&lt;/web-resource-name&gt;\n     * &lt;url-pattern&gt;/&lt;/url-pattern&gt;\n     * &lt;http-method&gt;TRACE&lt;/http-method&gt;\n     * &lt;/web-resource-collection&gt;\n     * &lt;auth-constraint/&gt;\n     * &lt;/security-constraint&gt;\n     */\n     Constraint constraint = new Constraint();\n     constraint.setName(\"Disable TRACE\");\n\n     ConstraintMapping mapping = new ConstraintMapping();\n     mapping.setConstraint(constraint);\n     mapping.setMethod(\"TRACE\");\n     mapping.setPathSpec(\"/\"); // this did not work same this mapping.setPathSpec(\"/*\");\n\n     ConstraintSecurityHandler securityHandler = (ConstraintSecurityHandler) servletHandler.getSecurityHandler();\n     securityHandler.addConstraintMapping(mapping);\n</code></pre>\n\n<p>Example output from soapUI:</p>\n\n<pre><code>HTTP/1.1 200 OK\nContent-Type: message/http\nContent-Length: 143\nServer: Jetty(9.0.6.v20130930)\n\nTRACE / HTTP/1.1\nConnection: keep-alive\nUser-Agent: Apache-HttpClient/4.1.1 (java 1.5)\nHost: 192.168.33.115\nAccept-Encoding: gzip,deflate\n</code></pre>\n", "answer_scores": {"34207095": 0, "29361924": 0.99341, "38005910": 0.0, "40990957": -0.621776, "29360239": -0.870892}}, "answer": {"owner": {"reputation": 1207, "user_id": 1754609, "user_type": "registered", "profile_image": "https://www.gravatar.com/avatar/73679d2587591c819dbdff89121c1664?s=128&d=identicon&r=PG", "display_name": "Jan", "link": "https://stackoverflow.com/users/1754609/jan"}, "is_accepted": true, "score": 2, "last_activity_date": 1450091327, "last_edit_date": 1450091327, "creation_date": 1427782882, "answer_id": 29361924, "question_id": 29348328, "body": "<p>On your <code>Constraint</code> object, you need to call <code>setAuthenticate(true)</code>, and ensure that you don't call <code>setRoles(String[])</code>. This makes it the equivalent of a <code>&lt;security-constraint&gt;</code> with an empty <code>&lt;auth-constraint&gt;</code>, which forbids access.</p>\n\n<p>The reason it works with the <code>DefaultServlet</code> and not the <code>CXFServlet</code> is because the <code>DefaultServlet</code> specifically denies access to the TRACE method.</p>\n"}}, {"index": 9, "question": {"tags": ["objective-c"], "owner": {"reputation": 18, "user_id": 1243448, "user_type": "registered", "profile_image": "https://www.gravatar.com/avatar/9564668a6530c229f7b40ec88c227336?s=128&d=identicon&r=PG", "display_name": "jamesdeacon", "link": "https://stackoverflow.com/users/1243448/jamesdeacon"}, "is_answered": true, "view_count": 233, "accepted_answer_id": 9522247, "answer_count": 2, "score": 1, "last_activity_date": 1330628352, "creation_date": 1330627784, "question_id": 9522137, "link": "https://stackoverflow.com/questions/9522137/are-java-files-supported-by-objective-cs-nsbundle-pathforresource-method", "title": "Are java files supported by Objective-C&#39;s NSBundle pathForResource method?", "body": "<p>I'm trying to obtain the path for a java file which I want to load into an NSString.</p>\n\n<p>Currently this line of code is returning nil.</p>\n\n<pre><code>[[NSBundle mainBundle] pathForResource:@\"LockDialog\" ofType:@\"java\"]];\n</code></pre>\n\n<p>I added my file \"LockDialog.java\" to the project via the menu, File>New>New File. The pathForResource method seems fine for returning the path of txt files or html files but completely fails when I'm trying to get the path of a java file.</p>\n\n<p>Any help or insight massively appreciated,</p>\n\n<p>Thanks,\nJames</p>\n", "answer_scores": {"9522259": 0.996875, "9522247": 0.996875}}, "answer": {"owner": {"reputation": 3356, "user_id": 260675, "user_type": "registered", "profile_image": "https://i.stack.imgur.com/XcIJz.png?s=128&g=1", "display_name": "Mike Fahy", "link": "https://stackoverflow.com/users/260675/mike-fahy"}, "is_accepted": false, "score": 3, "last_activity_date": 1330628352, "creation_date": 1330628352, "answer_id": 9522259, "question_id": 9522137, "body": "<p>File type should not matter, but chances are the file is not actually being copied to your application bundle. Check your Target>Build Phases>Copy Bundle Resources settings to ensure it's there, and if not, drag it over to this list.</p>\n"}}]
```

The final output is a JSON String.

## Running as Flask Server

```bash
python search.py
```
#### Output:

```
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-***-***
```
You can use any web browser to visit `http://localhost:5000`, where
`5000` is the default port of this application to open the search panel.

## Running on IBM Cloud Platform

The application is designed to run on IBM Cloud Platform without 
any changes to code, so you can [push the code](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-python-flask-mnist-tutorial.html#step4),
as is, using the CLI without any changes.
A [live instance](http://stacksearchhack.eu-gb.mybluemix.net/) is currently running on IBM Cloud Platform.

## Using the search panel

The search panel accepts query as input and shows 10 best results.

![Screenshot 1](images/Screenshot%20from%202019-06-23%2019-57-11.png)

![Screenshot 2](images/Screenshot%20from%202019-06-23%2019-57-41.png)

![Screenshot 3](images/Screenshot%20from%202019-06-23%2020-08-21.png)

# Documentation

The idea and concepts can be obtained from the [white paper](the_idea.pdf) and the method usages can be obtained from the [pydoc output](docs/search.html) of [search](search.py) module.

# Dependencies

It uses the [StackAPI](https://stackapi.readthedocs.io/en/latest/), 
[NetworkX Library](https://networkx.github.io/), 
[Natural Language ToolKit](https://www.nltk.org/)
and [IBM Watson Natural Language Understanding API](https://www.ibm.com/watson/services/natural-language-understanding/)
for obtaining data and determining relevant solutions. The 
application is designed as a [Flask](http://flask.pocoo.org/)
application, which can be run on Cloud Platforms, like 
Amazon Web Services and IBM Cloud Platform.
