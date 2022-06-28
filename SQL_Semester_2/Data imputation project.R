#Biblioteki
library(dplyr)
library(VIM)
library(laeken)

#Wczytanie danych
#Dane - NFL Combine - wyniki zawodników podczas combine, tj. meczu przed draftem
#Dane z okresu 2009-2019
data <- read.csv("NFL.csv", sep = ",")

#Zmienne:
#Year - rok
#Age - wiek zawodnika
#Height - wzrost w metrach
#Weight - waga zawodnika w kilogramach
#Sprint_40yd - czas sprintu na 40 jardów w sekundach
#Vertical_Jump - wysokoœæ skoku w pionie w centymetrach
#Bench_Press_Reps - maksymalna iloœæ powtórzeñ wyciskania sztangi na ³awce, sztanga wa¿¹ca 102.1 kg
#Broad_Jump - odleg³oœæ skoku w dal w centymetrach
#Agility_3cone - czas wykonania testu 3 ro¿ków na zwinnosæ w sekundach
#Shuttle - czas biegu pomiêdzy dwoma s³upkami w sekundach
#BMI - BMI (kg/m2)
#Player_Type - typ zawodnika
#Position_Type - typ pozycji, na której gra zawodnik
#Position - pozycja zawodnika
#Drafted - czy zawodnik zosta³ wybrany przez klub do profesjonalnej ligi w trakcie draftu

#Wybór tylko tych kolumn, którê s¹ potrzebne w projekcie
data <- data |> select(c(Year, Age, Height, Weight, Sprint_40yd, Vertical_Jump, 
                         Bench_Press_Reps, Broad_Jump, Agility_3cone, Shuttle, BMI, 
                         Player_Type, Position_Type, Position, Drafted))

#Odpowiedni zapis zmiennych
data$Year <- as.numeric(data$Year)
data$Player_Type <- as.factor(data$Player_Type)
data$Position_Type <- as.factor(data$Position_Type)
data$Position <- as.factor(data$Position)
data$Drafted <- recode(data$Drafted, "Yes" = 1, "No" = 0)
data$Drafted <- as.numeric(data$Drafted)
summary(data)

#Wykaz braków danych
plot_missing<-aggr(data, col=c('cyan','pink'),
                   numbers=TRUE, sortVars=TRUE,
                   labels=names(data), cex.axis=0.6,
                   cex.lab=1.5,
                   gap=1, ylab=c('Braki',"Wzór braków"))

#Regresyjna imputacja braków danych
data_imp <- data
data_imp <- regressionImp(Age+Agility_3cone+Shuttle+Bench_Press_Reps+Broad_Jump+Vertical_Jump+Sprint_40yd~Year+Height+Weight+BMI+Player_Type+Position_Type,
                          data=data_imp)
data_imp$Age <- round(as.numeric(data_imp$Age))
data_imp$Height <- round(as.numeric(data_imp$Height), digits = 2)
data_imp$Weight <- round(as.numeric(data_imp$Weight), digits = 1)
data_imp$Bench_Press_Reps <- round(as.numeric(data_imp$Bench_Press_Reps))
data_imp$Vertical_Jump <- round(as.numeric(data_imp$Vertical_Jump), digits = 2)
data_imp$Broad_Jump <- round(as.numeric(data_imp$Broad_Jump), digits = 2)
data_imp$Agility_3cone <- round(as.numeric(data_imp$Agility_3cone), digits = 2)
data_imp$Shuttle <- round(as.numeric(data_imp$Shuttle), digits = 2)
i=1
while (i<=nrow(data_imp)) {
  data_imp$Id[i] <- i
  i = i+1
}

#Wykaz braków danych po imputacji danych
plot_missing_imp<-aggr(data_imp, col=c('cyan','pink'),
                   numbers=TRUE, sortVars=TRUE,
                   labels=names(data_imp), cex.axis=0.6,
                   cex.lab=1.5,
                   gap=1, ylab=c('Braki',"Wzór braków"))
#Po imputacji danych braki nie wystêpuj¹

write.csv(data_imp,"dane_imputowane.csv", row.names = FALSE)

