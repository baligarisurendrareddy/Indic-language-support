# Import libraries
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Set font
hindi_font = fm.FontProperties(fname='Lohit-Hindi.ttf') 

# Take input 
hindi_text = input("कृपया हिंदी में कुछ लिखें: ")

# Print input
print(hindi_text)

# Plot input 
plt.rcParams['font.family'] = 'sans-serif'
plt.figure(figsize=(5,1)) 
plt.text(0.5, 0.5, hindi_text, fontproperties=hindi_font, size=20, ha='center')
plt.axis('off')
plt.tight_layout()
plt.show()