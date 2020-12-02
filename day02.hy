(defn stdin-to-list [f]
  (setv numbers [])
  (while True
      (try (.append numbers (-> (input) f))
          (except [Exception] (break))))
  (return numbers)
)

(defn parse [line]
  (-> (.replace line ":" "")
      (.replace "-" " ")
      (.split)))

(setv parsed (stdin-to-list parse))

(defn valid1 [line]
  (setv n (.count (get line 3) (get line 2)))
  (setv lo (int (get line 0)))
  (setv hi (int (get line 1)))
  (and (<= lo n) (>= hi n)))

(-> (map valid1 parsed)
    (sum)
    (print))

(defn valid2 [line]
  (setv cs (get line 3))
  (setv c (get line 2))
  (setv lo (- (int (get line 0)) 1))
  (setv hi (- (int (get line 1)) 1))
  (!= (= (get cs lo) c) (= (get cs hi) c)))

(-> (map valid2 parsed)
    (sum)
    (print))
