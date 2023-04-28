import Foundation
import XCTest
@testable import TopLeet

final class RomanToIntTests: XCTestCase {
    private var romanToInt: RomanToInt?

    override func setUpWithError() throws {
        romanToInt = RomanToInt()
    }

    override func tearDownWithError() throws {
        romanToInt = nil
    }

    func test_1() throws {
        // When
        let numeral = "III"
        
        // Then
        XCTAssertEqual(romanToInt?.execute(for: numeral), 3)
    }

    func test_2() throws {
        // When
        let numeral = "LVIII"
        
        // Then
        XCTAssertEqual(romanToInt?.execute(for: numeral), 58)
    }
    
    func test_3() throws {
        // When
        let numeral = "MCMXCIV"
        
        // Then
        XCTAssertEqual(romanToInt?.execute(for: numeral), 1994)
    }
}
