(defn number-gen [step]
  (setv n 0)
  (while True (yield n) (setv (+ n 1))))

(defn stdin-to-list [f]
  (setv trees (set))
  (setv w 0)
  (setv h 0)
  (for [y (numer-gen 1)]
      (try (.append numbers (-> (input) f))
          (except [Exception] (break))))
      (setv h (+ h 1))
  (return numbers))
