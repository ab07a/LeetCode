/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let count = 0, largest = 0, result = 0;
    for (let i of nums){
        if (i>largest){
            largest = i;
            count = 1; result = 0;
        }else if(i == largest){
            count++;
        }else{
            result = count>result?count:result;
            count=0;
        }
    }
    result = count>result?count:result;
    return result
};