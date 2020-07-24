# questions
# test cases

# 1. Understand the Problem (15min)
# 2. Plan (15min)
# 3. Execute/Pass Tests Cases (30 min)

# Condensed List
/*
#  * Complete the 'condense' function below.
#  *
#  * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
#  * The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#  */

# /*
#  * For your reference:
#  *
#  * SinglyLinkedListNode {
#  *     int data;
#  *     SinglyLinkedListNode next;
#  * }
#  *
#  */

# function condense(head) {
#     // Write your code here


# function main() {
#     const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

#     let head = new SinglyLinkedList();

#     const headCount = parseInt(readLine().trim(), 10);

#     for (let i = 0; i < headCount; i++) {
#         const headItem = parseInt(readLine().trim(), 10);
#         head.insertNode(headItem);
#     }

#     const result = condense(head.head);

#     printSinglyLinkedList(result, '\n', ws);
#     ws.write('\n');

#     ws.end();
# }