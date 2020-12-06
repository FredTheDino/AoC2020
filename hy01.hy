(import [itertools [combinations :as comb]])
(import sys)

(setv numbers [])
(while True
    (try (.append numbers (-> (input) int))
        (except [Exception] (break))))

(defn first-match [f l]
    (for [x l] (when (f x) (return x))))

(defn prod [xs]
    (reduce (fn [a x] (* a x)) xs 1))

(->> (comb numbers 2)
     (first-match
         (fn [x] (= 2020 (sum x))))
     prod
     print)

(->> (comb numbers 3)
     (first-match
         (fn [x] (= 2020 (sum x))))
     prod
     print)
