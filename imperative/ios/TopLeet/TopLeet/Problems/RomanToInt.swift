import Foundation

// https://leetcode.com/problems/roman-to-integer/
struct RomanToInt {
    func execute(for romanNumeral: String) -> Int {
        var result = 0
        
        let romanNumeralMap: [Character: Int] = [
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        ]
        
        if romanNumeral.count == 1 {
            return romanNumeralMap[romanNumeral.first ?? " "] ?? -1
        }
        
        for i in 0..<romanNumeral.count {
            if i == romanNumeral.count - 1 {
                guard let firstValue = romanNumeralMap[romanNumeral[romanNumeral.index(romanNumeral.startIndex, offsetBy: i)]] else { return -1 }
                result += firstValue
                break
            }
            
            guard let firstValue = romanNumeralMap[romanNumeral[romanNumeral.index(romanNumeral.startIndex, offsetBy: i)]], let secondValue = romanNumeralMap[romanNumeral[romanNumeral.index(romanNumeral.startIndex, offsetBy: i + 1)]] else { return -1 }
            
            if firstValue >= secondValue {
                result += firstValue
                continue
            }
            
            result -= firstValue
        }
        
        return result
    }
}
