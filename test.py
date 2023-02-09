def numberToWords(n): 
  # strings at index 0 is not used,  
  # it is to make array indexing simple  
  ones = ["", "One ", "Two ", "Three ", "Four ", 
          "Five ", "Six ", "Seven ", "Eight ", 
          "Nine ", "Ten ", "Eleven ", "Twelve ",  
          "Thirteen ", "Fourteen ", "Fifteen ",  
          "Sixteen ", "Seventeen ", "Eighteen ", 
          "Nineteen "] 
    
  # strings at index 0 and 1 are not used, 
  # they are to make array indexing simple 
  tens = ["", "", "Twenty ", "Thirty ", "Forty ", 
          "Fifty ", "Sixty ", "Seventy ", "Eighty ",  
          "Ninety "] 
    
  # If n is in range of 19, 
  # then directly return the value 
  if (n < 20): 
      return ones[n] 

  # If n is in range of 20-99 
  if (n < 100): 
      return tens[n // 10] + numberToWords(n % 10) 

  # If n is in range of 100-999 
  if (n < 1000): 
      return ones[n // 100] + "Hundred " + numberToWords(n % 100) 

  # If n is in range of 1000-9999 
  if (n < 10000): 
      return ones[n // 1000] + "Thousand " + numberToWords(n % 1000) 

  # If n is in range of 10000-99999 
  if (n < 100000): 
      return tens[n // 10000] + numberToWords(n % 10000) 

  # If n is in range of 100000-999999 
  if (n < 1000000): 
      return ones[n // 100000] + "Hundred " + numberToWords(n % 100000) 

  # If n is in range of 1000000-9999999 
  if (n < 10000000): 
      return ones[n // 1000000] + "Million " + numberToWords(n % 1000000) 
  
# Driver Code 
# n = int(input("Enter a number: "))
print(numberToWords(123456789))