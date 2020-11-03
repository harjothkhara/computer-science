// initial try - fail!
function maximumContainers(scenarios) {
  let newContainers = 0
    // console.log(scenarios[0])
    scenarios.forEach(scenario => {
        console.log(scenario.split(' ')[0])
        // max num of conatiners we can buy with our budget
        newContainers += scenario.split(' ')[0] / scenario.split(' ')[1]
        // how many can we send back for a free container?
        let freeContainer = 1 + (newContainers - scenario.split(' ')[2]) 
        
        // if(freeContainer > 0){
        //     newContainers -= scenerio[2]
        // }
         
         return newContainers += freeContainer
    })
   
}

// next day solution
function maximumContainers(scenarios) {
  scenarios.forEach(scenario => {
      let n = scenario.split(' ')[0]
      let c = scenario.split(' ')[1]
      let m = scenario.split(' ')[2] // 
      
      let containers = Math.floor(n/c) // purchased
      let emptyContainers = containers 
      
      while(emptyContainers >= m){
          containers += Math.floor(emptyContainers/m)
          emptyContainers = Math.floor(emptyContainers/m + emptyContainers%m)
        }
      return containers
  })
 
}

const scenarios = ['10 2 5', '12 4 4', '6 2 2']
                    // 6        3         5
maximumContainers(scenarios)