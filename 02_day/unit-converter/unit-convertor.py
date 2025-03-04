import streamlit as st

def convert_unit(value,unit_from, unit_to):
    conversion = {
        'meters_kilometers':0.001, # 1 meterr = 0.001 kilometer
        'kilometers_meters':1000, # 1 kilometer = 1000 meter
        'grams_kilograms':0.001, # 1 gram = 0.001 kilogram
        'kilograms_grams':1000, # 1 kilogram = 1000 gram
    }
    key = f'{unit_from}_{unit_to}' # generate a key for converrstion (based on input and output)
    if key in conversion:
        conversion = conversion[key]
        return value * conversion
    else:
        return 'Convertion not Supported'
    
st.title('Unit Convertor')
value = st.number_input('Enter the value')
    
unit_from = st.selectbox('Convert from:', ['meters','kilometers', 'grams', 'kilograms'])
unit_to = st.selectbox('Convert to',  ['meters', 'kilometers', 'grams', 'kilograms'])
if st.button('convert'):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f'Converted value {result}')
        
    
# if (__name__=='__main__'):
#        convert_unit()
    

