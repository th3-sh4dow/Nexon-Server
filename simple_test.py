#!/usr/bin/env python3
"""
Simple Test for Multiple Commands
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Backend'))

try:
    from Backend.Model import FirstLayerDMM
    print("✅ Successfully imported FirstLayerDMM")
    
    # Test the complex query
    test_query = "nexon open whatsapp and play a song name ham mere safer and set volum into 90%"
    print(f"\n🔍 Testing: {test_query}")
    
    result = FirstLayerDMM(test_query)
    print(f"📤 Result: {result}")
    
    # Test another query
    test_query2 = "nexon open whatsapp play song name pal pal and set voloume into 50%"
    print(f"\n🔍 Testing: {test_query2}")
    
    result2 = FirstLayerDMM(test_query2)
    print(f"📤 Result: {result2}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc() 