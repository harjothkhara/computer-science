function closest(s, queries) {
  let queryResult = [];
  // char at current query that we're checking
  queries.forEach((query) => {
    // have a pointer at the current query
    let currQuery = s[query];
    let left = query - 1;
    let right = query + 1;
    // iterate to the left and right of it until you reach the end of the string
    while (left > 0 || right < s.length) {
      // at each left and right index, check if the char matches the char for the given query
      if (s[left] === currQuery || s[right] === currQuery) {
        // if both sides match then print the left side(lowest) index
        if (s[left] === currQuery && s[right] === currQuery) {
          queryResult.push(left);
          return left;
        }
        // else print the matching index
        else if (s[left] === currQuery) {
          queryResult.push(left);
          return left;
        } else if (s[right] === currQuery) {
          queryResult.push(right);
          return right;
        }
      }
      left--;
      right++;
    }
    // print -1 since we've checked the left and right side of string and char index query not found
    queryResult.push(-1);
    return -1;
  });
  return queryResult;
}
