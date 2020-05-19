### Short Answer

- Explain how the CPU provides concurrency or parallelism:

* how CPU does more than one thing at a time
* concurrency is when tasks can start, run, and complete in overlapping time period, an application is making progress on more than one task at the same time concurrently.
* parallelism is when a task is split into smaller sub-tasks which literally run at the same time, for instance on multiple CPUs at the exact time\
* concurrency is related to how an application handles multiple tasks it works on
* Parallelism on the other hand, is related to how an application handles each individual task
* an application can be concurrent, but not parallel (processed more than one task at a time but the thread is only executing on one task at a time)
* an application can also be parallel but not concurrent (one task at a time, and this task is broken down into subtasks which can be processed in parallel)

  http://tutorials.jenkov.com/java-concurrency/concurrency-vs-parallelism.html

- Describe assembly language and machine language:
  assembly language is low-level language that needs a compiler and interpreter, which converts that language to machine language that the computer can understand. machine language is a series of bit patterns that is the binary form that are directly executed by the computer.

### Number Conversions

Add the answers to `ANSWERS.md`.

- Convert `11001111` binary to hex:

  # fist cut the binary number in half

         1100 1111
         8,4 + 8,4,2,1
         12     15
         C       F

           0xCF
       hex has 16 possible digits
       0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
                               |     |
                               12    15

  to decimal:

  # 11001111

       11001111

  128,64 8,4,2,1
  192 + 15

        207

- Convert `4C` hex

  to binary:
  4 C
  4 12
  0100 1100

        0b01001100

  to decimal:
  4 C
  4 12
  0100 1100 # use binary route as in-between
  64 8,4
  64 + 12 = 76

        76

* Convert `68` decimal

            to binary:
            ||||  ||||

          8 bits so can start at:
          2^7=128, 2^6=64, 2^5=32, 2^4=16, 2^3=8, 2^2=4

            0100  0100

            0b01000100

  to hex:

          use binary route as in-between
          0100 0100
           4     4
             0x44
