// Conversion of python to typescript, see python file for methodology

function twoSum(nums: number[], target: number): number[] {
    var numbers = {}

    for(let i = 0; i < nums.length; i++) {
        if(nums[i] in numbers) {
            return [numbers[nums[i]], i]
        } else {
            numbers[target - nums[i]] = i
        }
    }
    
    return []
};