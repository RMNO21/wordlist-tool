def run():

    ############################################################################################
    # Copyright (C) 2025 Raman Tondro
    #
    # This program is free software; you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation; either version 2 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program; if not, write to the Free Software
    # Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
    ############################################################################################

    from itertools import permutations
    from itertools import product
    import time



    print(r"""                                        
    ██     ██  ██████  ██████  ██████      ██      ██ ███████ ████████ 
    ██     ██ ██    ██ ██   ██ ██   ██     ██      ██ ██         ██    
    ██  █  ██ ██    ██ ██████  ██   ██     ██      ██ ███████    ██    
    ██ ███ ██ ██    ██ ██   ██ ██   ██     ██      ██      ██    ██    
    ███ ███   ██████  ██   ██ ██████      ███████ ██ ███████    ██    
                                                                    
                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                    
    """
    )
    #by Raman Tondro


    def loopnum():
        loop=int(input("enter the loop number: "))   
        if 0 < loop and 11 > loop:
            return loop
        else:
            print("the loop must be between <1> and <10> ")
            loopnum()
    a=[]
    c=0
    print("enter the possible words ")
    print("enter the possible words (use ',' for OR options)")
    print("print <done> or when blank, press <enter> to complete ")

    b=' '



    while (b!= 'done' and b!=''):

        b=(input(f"{c+1}: "))
        if b=="done" or b=='':
            break
        a.append([x.strip() for x in b.split(',')])
        c+=1
    loop=loopnum()
    sep=input("enter the seperator, like '@' , '$' , '&' ... : (press enter to fill blank) ")
    for i in range(loop):
        for combo in permutations(range(c), i+1): 
            for alt in product(*[a[x] for x in combo]):
                print(sep.join(alt))

                        
            


