

image foresta bg = "tronchi.png"
image foresta blu = "forestablu.png"
image brown = "background.png"
image grande quercia = "lagrandequercia.png"

image mordecai = "mordecai.png"
image tiziano = "tiziano.png"
image tiziano felice = "tizianofelice.png"
image margherita = "margherita.png"
image margherita felice = "margheritafelice.png"
image giorgio = "giorgio.png"
image giorgio felice = "giorgiofelice.png"
image oggetti = "oggetti.png"
image diodellaforesta = "diodellaforesta.png"


define Mordecai = Character('Mordecai', color="#c8ffc8")
define Tiziano = Character('Tiziano', color="#ffffff")
define Margherita = Character('Margherita', color="#ffffff")
define Giorgio = Character('Giorgio', color="#ffffff")
define Diodellaforesta = Character('Dio della Foresta', color="#ffffff")



label start:
    
    scene foresta bg
    
    show mordecai

    "Tu sei Mordecai la Cornacchia."
    "Ti piace moltissimo collezionare tesori!"
    "Tuttavia, la tua passione è diventata avidità."
    "La tua casa è stata infestata dai conigli, e ti devi trasferire temporaneamente nella Grande Quercia."
    
    hide mordecai
    show oggetti
    
    "Ci sono tre oggetti nella tua borsa: un ciondolo di lacrime di drago, un libro e un dinosauro pelouche."
    
    scene grande quercia
    hide oggetti
    
    "Finalmente, hai raggiunto la grande quercia."
    
    show tiziano
    
    "Quando entri al piano terra, noti una talpa seduta vicino a un buco nella terra."
    
    menu:
        "Avvicinati":
            jump scenaTalpa1
        "Ignorala":
            jump sezioneStoria1
    
    
    
label sezioneStoria1:
    
    hide tiziano
    
    "Cammini dritto, salendo le scale all'interno della quercia, quando senti uno strano suono provenire dalla porta alla tua sinistra."
    
    menu:
        "Bussa alla porta":
            jump scenaTopo1
        "Ignoralo":
            jump sezioneStoria2


    
label sezioneStoria2:
    
    "Mentre vai alla tua stanza, senti dei singhiozzi provenire da una delle porte."
    
    menu:
        "Bussa alla porta":
            jump scenaGufo1
        "Ignorali":
            jump sezioneStoria3
            
            
            
label sezioneStoria3:
    
    "La notte successiva, decidi di fare un altro giro per la Grande Quercia."
    
    "Mentre stai andando al piano terra, noti sul pavimento un volantino per un Club del Libro!"
    
    show tiziano
    
    "Al piano terra, vedi di nuovo la talpa. Stavolta sembra ancora più preoccupata."
    
    hide tiziano
    
    menu:
        "Parli con la talpa":
            jump scenaTalpa2
        "Ignori la talpa":
            $ lacrime = False
            jump sezioneStoria4



label sezioneStoria4:
    
    "Continui per la tua strada, finché non senti degli squittii provenire da una porta."
    
    menu:
        "Bussi alla porta":
            jump scenaTopo2
        "Ignori gli squittii":
            $ pelouche = False
            jump sezioneStoria5


label sezioneStoria5:
    
    "Mentre stai andando verso la tua stanza, senti dei singhiozzi provenire da un'altra porta..."
    
    menu:
        "Apri la porta":
            jump scenaGufo2
        "Ignori i singhiozzi":
            $ libro = False
            jump fine
            
            
            
            
            
label scenaTalpa1:
    
    Tiziano "Ciao. Io sono Tiziano la Talpa."
    
    hide tiziano
    show mordecai
    
    Mordecai "A che serve quel buco nel pavimento?"
    
    hide mordecai
    show tiziano
    
    Tiziano "Oh, uh... è un buco nero che porta al pozzo sotterraneo."
    
    Tiziano "Dovrei andare a prendere l'acqua, ma... è tutto buio lì sotto..."
    
    hide tiziano
    
    "Dopo aver detto ciao a Tiziano, continui per la tua strada..."
    
    jump sezioneStoria1
    
    

label scenaTopo1:
    
    "Bussi alla porta..."
    
    show mordecai
    
    Mordecai "Va tutto bene lì dentro?"
    
    "Senti dei rumori e la porta si apre."
    
    hide mordecai
    show margherita
    
    Margherita "Sì... Va tutto bene... Grazie..."
    
    Margherita "Io sono Margherita il Topolino... E tu?"
    
    hide margherita
    show mordecai
    
    Mordecai "Io sono Mordecai."
    
    hide mordecai
    show margherita
    
    Margherita "E' un bel nome... Beh, grazie..."
    
    hide margherita
    
    "Dopo aver detto ciao a Margherita, continui per la tua strada..."
    
    jump sezioneStoria2
    
    
    

            
            
            
label scenaGufo1:
    
    "Bussi alla porta"
    
    show mordecai
    
    Mordecai "E' tutto a posto lì dentro?"
    
    "La porta si apre."
    
    hide mordecai
    show giorgio
    
    Giorgio "Oh *sniff* Sto quasi bene, grazie... Io sono Giorgio il Gufo, e tu?"
    
    hide giorgio
    show mordecai
    
    Mordecai "Io sono Mordecai."
    
    hide mordecai
    show giorgio
    
    Giorgio "Grazie per essere venuto a salutarmi. Ci vediamo in giro, Mordecai. Hooooo~"
    
    hide giorgio
    
    "Saluti Giorgio il Gufo e vai verso la tua stanza."
    
    jump sezioneStoria3
    
    
    

    
    
    
label scenaTalpa2:
    
    hide tiziano
    show mordecai
    
    Mordecai "Tiziano, che succede?"
    
    hide mordecai
    show tiziano
    
    Tiziano "Ho così tanta paura del buio... ma se non vado a prendere l'acqua, mi cacceranno dalla Grande Quercia! Sono così spaventato..."
    
    hide tiziano
    show oggetti
    
    "Ti ricordi che nella tua borsa hai il ciondolo di lacrime di drago. Le lacrime di drago producono luce, e possono illuminare la strada attraverso l'oscurità più fitta."
    
    menu:
        
        "Dai le lacrime di drago a Tiziano":
            
            $ lacrime = True
            hide oggetti
            show tiziano felice
            
            Tiziano "Lacrime di drago?! Ma come...?! Grazie Mordecai, questo è proprio quello che mi serviva!"
            
            hide tiziano felice
            jump sezioneStoria4
            
        "Non dare le lacrime di drago a Tiziano":
            
            $ lacrime = False
            hide oggetti
            
            "Sorridi impietosito alla talpa e vai via."
            
            jump sezioneStoria4
            
            
            

            
            
            
label scenaTopo2:
    
    show mordecai
    
    Mordecai "Ehi, è tutto a posto?"
    
    "Non c'è nessuna risposta, ma gli squittii aumentano."
    
    "Apri la porta."
    
    hide mordecai
    show margherita
    
    Margherita "C'è un mostro sotto il mio letto! Sono sicura che appena mi addormenterò, mi prenderà!"
    
    Margherita "Vorrei così tanto avere un pelouche da abbracciare... sono così spaventata!"
    
    hide margherita
    show oggetti
    
    "Ti ricordi di avere un piccolo dinosauro pelouche in borsa."
    
    menu:
        
        "Dai il pelouche a Margherita.":
            
            $ pelouche = True
            
            hide oggetti
            show margherita felice
            
            Margherita "Questo dinosauro è perfetto, Mordecai! Grazie mille!"
            
            hide margherita felice
            
            jump sezioneStoria5
            
        "Non dare il pelouche a Margherita.":
            
            $ pelouche = False
            
            hide oggetti
            show mordecai
            
            "Controlli sotto il letto di Margherita."
            
            Mordecai "Non c'è niente sotto il tuo letto, Margherita."
            
            hide mordecai
            
            "Ma Margherita ha ancora paura."
            
            "Decidi di lasciare la sua stanza."
            
            jump sezioneStoria5
            
            
            

            

label scenaGufo2:
    
    hide mordecai
    show giorgio
    
    Giorgio "Hoooo~ "
    
    Giorgio "Ciao Mordecai... *sniff* Stavolta non posso nascondertelo..."
    
    Giorgio "Mi sento molto solo... Vorrei avere un modo per farmi degli amici!"
    
    hide giorgio
    show oggetti
    
    "Ricordi di aver visto il volantino per il Club del Libro, e di avere il libro che stanno leggendo in borsa. Un Club del Libro potrebbe essere un ottimo modo per Giorgio per farsi degli amici!"
    
    menu:
        "Dai a Giorgio il libro":
            $ libro = True
            hide oggetti
            show giorgio felice
            Giorgio "Un Club del Libro? Idea meravigliosa, Mordecai, grazie mille!"
            hide giorgio felice
            jump fine
        "Non dare a Giorgio il libro":
            $ libro = False
            hide oggetti
            "Ti senti un po' triste e dai a Giorgio una pacca sulla spalla"
            jump fine
            

label fine:
    
    "Continui ad andare verso la tua stanza..."
    
    "..."
    
    "Il giorno successivo..."
    
    "Un piccione viaggiatore arriva portandoti la notizia che puoi tornare a casa!"
    
    "Mentre lasci la grande quercia, un vento forte ti avvolge, e ti accorgi che il paesaggio sta cambiando..."
    
    scene foresta blu
    
    show diodellaforesta
    
    Diodellaforesta "Mordecai, ho osservato il tuo comportamento per anni..."
    
    if lacrime and pelouche and libro:
        Diodellaforesta "Il tuo cuore era un tempo consumato dall'avidità."
        Diodellaforesta "Ma tramite la tua gentilezza, il tuo cuore è cambiato."
    else:
        Diodellaforesta "Ho sperato che il tuo cuore avido cambiasse..."
        Diodellaforesta "Ma devi ancora fare molta strada..."
    
    if lacrime: 
        hide diodellaforesta
        show tiziano felice
        Diodellaforesta "Grazie alla tua gentilezza, Tiziano la Talpa ora non ha più paura del buio, e ha ancora un posto che può chiamare casa."
        hide tiziano felice
    else:
        hide diodellaforesta
        show tiziano
        Diodellaforesta "Tiziano la Talpa è stato cacciato fuori dalla sua casa."
        hide tiziano
    
    if libro:
        show giorgio felice
        Diodellaforesta "Grazie a te, Giorgio il Gufo ora fa parte del Club del Libro ed è diventato amico di Margherita."
        hide giorgio felice
    else:
        show giorgio
        Diodellaforesta "Giorgio il Gufo è rimasto solo e senza amici."
        hide giorgio
    
    if pelouche:
        show margherita felice
        Diodellaforesta "E Margherita il Topolino ora dorme tranquillamente, con Giorgio che veglia sul suo sonno."
        hide margherita felice
    else:
        show margherita
        Diodellaforesta "Margherita il Topolino è scomparsa senza lasciare traccia."
        hide margherita
    
    show diodellaforesta
    Diodellaforesta "Gli atti di gentilezza, non importa se siano grandi o piccoli, possono significare molto più di quello che immagini."
    
    if not lacrime and not pelouche and not libro:
        Diodellaforesta "Fai le tue scelte con più attenzione la prossima volta, Mordecai."
    
    
    
    
