struct PalindromicSubstring {
    func countSubstrings(_ s: String) -> Int {
        var result = s.count
        var before = 0
        var after = 0
        
        let sArr = Array(s)
        
        for i in 0..<sArr.count {
            // odd
            before = i - 1
            after = i + 1
            while after < sArr.count && before >= 0 {
                if sArr[before] != sArr[after] {
                    break
                }
                result += 1
                before -= 1
                after += 1
            }
            
            // even
            before = i
            after = i + 1
            while after < sArr.count && before >= 0 {
                if sArr[before] != sArr[after] {
                    break
                }
                result += 1
                before -= 1
                after += 1
            }
        }
        
        return result
    }
}
