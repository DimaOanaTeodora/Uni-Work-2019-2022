import Prelude hiding (lookup)
import qualified Data.List as List
import Data.List
import Test.QuickCheck
import Numeric.Natural
import Data.Char
import Data.List (nub)
import Data.Maybe (fromJust)
import Test.QuickCheck
import Test.QuickCheck.Gen
import Data.Monoid
import Data.Semigroup (Max (..), Min (..))
import Data.Foldable (foldMap, foldr)
import Data.Char (isUpper)
import Data.List (nub)
{-
data Reteta =  Stop | R Ing Reteta
         deriving  Show

data Ing = Ing String Int
         deriving Show
--Punctul a)
--Ma folosesc de mai multe functii auxiliare

--transforma un string in string cu litere mici
r00do :: String -> String
r00do str = [ toLower loweredString | loweredString <- str]

--lista de ingrediente unice
r01do ::Reteta -> [String]
r01do Stop=[]
r01do (R (Ing nume cant) r )= nub ([r00do nume] ++ r01do r)

--pt un ingredient intoarce valorile din reteta
r02do :: Reteta -> String -> [ Int]
r02do Stop _ =[]
r02do (R (Ing nume cant) r ) ingredient = [ cant | (r00do ingredient) ==(r00do nume)] ++ r02do r ingredient

--pt o reteta si un ingredient intoarce cant maxima a ingredientului
r03do:: Reteta -> String -> Int
r03do reteta ingredient =maximum (r02do reteta ingredient)

--pt o lista de ingrediente si o reteta intoarce retetea conf enuntutlui
r04do :: [String] -> Reteta -> Reteta
r04do [x] reteta = R (Ing x (r03do reteta x )) Stop
r04do l Stop = Stop
r04do (h:t) reteta = R (Ing h (r03do reteta h )) (r04do  t reteta)

--cerinta punctul a)
r11do :: Reteta -> Reteta
r11do reteta = r04do (r01do reteta) reteta

--Teste
-- *Main> r11do (R  (Ing "faina" 500) (R  (Ing "Oua" 4) (R (Ing "faina" 300) Stop)))
--R (Ing "faina" 500) (R (Ing "oua" 4) Stop) 

-- *Main> r11do (R  (Ing "faina" 500) (R  (Ing "Oua" 4) (R (Ing "zahar" 200) Stop)))
-- R (Ing "faina" 500) (R (Ing "oua" 4) (R (Ing "zahar" 200) Stop))

--Punctul b)
--instance Eq Reteta where
    --(==) r1 r2 = (r01do r1) == (r01do r2) 
    --listele de ingrediente sa fie egale si daca sunt caut sa vad ingredientele sa aiba aceeasi cantitate 
    --da eroare de indentare si nu stiu de ce 
    --(==) (R (Ing nume1 cant1) r1 ) (R (Ing nume2 cant2) r2 ) = if (((r01do r1) == (r01do r2))==True ) then  foldr (\nume curent -> (((r03do (R (Ing nume1 cant1) r1 ) nume ) ==(r03do (R (Ing nume2 cant2) r2 ) nume ) )&& curent ) True (r01do r1 ) else False


--r1 =  R (Ing "faina" 500) (R (Ing "oua" 4) (R  (Ing "zahar" 500) (R (Ing "faina" 300) Stop)))
--r2 =  R (Ing "fAIna" 500) (R (Ing "zahar" 500) (R (Ing "Oua" 4) Stop ))
--r3 =  R (Ing "fAIna" 500) (R (Ing "zahar" 500) (R  (Ing "Oua" 55) Stop))

--Punctul c)

data Arb = Leaf Int String | Node Arb Int String Arb
        deriving  Show
r22do :: Arb -> Reteta 
r22do (Leaf cantitate nume)= R (Ing nume cantitate) Stop
r22do (Node arb1 cantitate nume arb2 ) = R (Ing nume cantitate) (R (Ing nume cantitate)(r22do arb2))

-}
data B e = R e Int | B e ::: B e
    deriving Eq
    
infixr 5 :::
{-
instance Foldable B where
    foldMap f = go
        where
        go (R e a) = f a
        go ((B e1) ::: (B e2)) = (go e1) ::: (go e2) 
 
fTest0 = maximum (R "nota" 2 ::: R "zece" 3 ::: R "la" 5 ::: R "examen" 1) == "zece"
cTest0 = cFilter (\x -> length x == 4) (fromList [“nota”, “zece”, “la”, “examen”]) ==
     (R (Just “nota”) 1 ::: R (Just “zece”) 2 ::: R Nothing 3 ::: R Nothing 4)
-}
class C e where
  cFilter :: (a -> Bool) -> e a -> e (Maybe a)
  fromList :: [a] -> e a
instance C B where
    cFilter p (R e x) = if( p (R e x) == True) then (R e Just x) else (R e Nothing)
  




{-
data PairInt=P Int Int
    deriving (Show)
--lista de perechi
data MyList=L [PairInt]
    deriving (Show)
--expresii formate din nr intregi si op de adunare si inmultire
data Exp = I Int | Add Exp Exp | Mul Exp Exp
class MyClass m where
    toExp::m -> Exp
instance MyClass MyList where
    --toExp list= ff (fun list )
    -- toExp ( L []) = I 1
    toExp ( L [ P n m]) = Add (I n) ( I m)
    toExp ( L ( ( P n m): xs )) = Mul ( Add (I n) (I m )) ( toExp (L xs))
p1=toExp ( L [ P 1 2, P 2 3 , P 5 3])

--functie auziliara transforma o lista de perechi intr=o lista de tupluri
fun :: MyList -> [(Int, Int)]
fun (L l) = [ (x,y)| (P x y)<-l ]
--functie auxiliara transforma o lista de tupluri intr-o expresie
ff :: [(Int, Int)] -> Exp
ff [(x,y)]= Add (I x) (I y)
ff (h:t)= Mul (Add (I (fst h)) (I (snd h))) (ff t) 

instance Show Exp where
    show (I n)= show n
    show (Add e1 e2)= "("++show e1 ++ "+" ++ show e2 ++")"
    show (Mul e1 e2)=  "("++show e1 ++ "*" ++ show e2++")" 
    -}