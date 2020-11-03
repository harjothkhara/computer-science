function perfectTeam(skills) {
  // idea:
  // see if all the skills exists
     // if they do, then find the min number of all the skills = total # of teams

  // plan:
 // store the letter and frequeny as a key/value inside a hashmap
 // loop through string
    // if char already exists in the map then increment the value(occurance) by 1  
    //else store each char in the map

// map = {'p':1, 'c':2, 'm':2, 'b':3, 'z':1}
// iterate through the values of the map and return the min value = total teams that can be created

    let map = new Map()
    
    for(let char of skills){
        if(map.has(char)){
            map.set(char, map.get(char)+1)
        } else {
            map.set(char, 1)
        }
    }
    if(!map.has('p') || !map.has('c') || !map.has('m') || !map.has('b') || !map.has('z')) return 0
    return Math.min(...map.values())
}