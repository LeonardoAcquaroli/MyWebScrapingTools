indicatori_del_numero = '(tel|telefono|numero|centralino|contatto|fisso)'
spazi_e_caratteri_nonwords_dopo_indicatore = '[^(a-zA-Z0-9)](.*)'
prefisso = '(0[0-9])'
iteration_num_space = "([^(a-zA-Z0-9)]?)([0-9]+[^(a-zA-Z0-9\&\<\>\(\)\;)]?)+" 
PHONE_REGEX_specific = indicatori_del_numero + spazi_e_caratteri_nonwords_dopo_indicatore + prefisso + iteration_num_space
phone_regex = "^(?:\+39\s)?\d{2,3}[\s.-]?\d{6,7}$"
EMAIL_REGEX = "[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"