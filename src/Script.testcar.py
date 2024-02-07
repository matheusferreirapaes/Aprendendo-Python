carros_mais_caros_do_mundo ={

     'rolls-royce_boat_tail':{
         'preço_milhões':147,
         'cavalos':571,
     },

     'bugatti_la_voiture_noire':{
         'preço_milhões':19,
         'cavalos':1500,
     },
     'rolls-royce_sweptail':{
         'preço_milhões':68,
         'cavalos':460,
     },
     'bugatti_centodieci':{
         'preço_milhões':48,
         'cavalos':1600,
     },
      'mercedes_maybach_exelero':{
         'preço_milhões':8,
         'cavalos':700,
     },

      'sp_automotive_chaos':{
         'preço_milhões':34,
         'cavalos':2077,
     },
      'bugatti_divo':{
         'preço_milhões':30,
         'cavalos':1500,
     },

      'bugatti_bolide':{
         'preço_milhões':25,
         'cavalos':1600,
     },
      'lamborghini_veneno_roadster':{
         'preço_milhões':24,
         'cavalos':750
     },

      'bugatti_chiron_super_sport_300':{
         'preço_milhões':20,
         'cavalos':1600,
     },

      'lamborghini_sián':{
         'preço_milhões':4,
         'cavalos':819,
     },

      'bugatti_chiron_pur_sport':{
         'preço_milhões':19,
         'cavalos':1600,
     },

      'pagani_huayra_roadster_bc':{
         'preço_milhões':18,
         'cavalos':811,
     },

      'w_motors_lykan_hypersport':{
         'preço_milhões':18,
         'cavalos':791,
     },

      'aston_martin_valkyrie':{
         'preço_milhões':17,
         'cavalos':1200,
     },
}


preço = carros_mais_caros_do_mundo['rolls-royce_boat_tail']['preço_milhões']- carros_mais_caros_do_mundo['aston_martin_valkyrie']['preço_milhões']
cavalos = carros_mais_caros_do_mundo['sp_automotive_chaos']['cavalos']- carros_mais_caros_do_mundo['rolls-royce_sweptail']['cavalos']
msg1 = 'podemos perceber a diferença de preço do rolls royce, para um aston'
msg2 = 'podemos perceber a diferença de cavalos do sp automotive, para um rolls royce'
msg3 = 'acompenhe a lista dos 15 carros mais caros do mundo'
msg4 = 'obrigado por acompanhar a gente na lista de carros mais caros do mundo!'
msg5 = 'milhões'
msg6 = 'cavalos'

print(msg3, carros_mais_caros_do_mundo)

print(msg1, preço, msg5)

print(msg2, cavalos, msg6)

print(msg4)

