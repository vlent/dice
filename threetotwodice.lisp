(defun tri (n)
  "triangular number"
  (/ (* n (+ n 1)) 2))

(defun tet (n)
  "tetrahedral number"
  (/ (* n (+ n 1) (+ n 2)) 6))

(defun num* (i j k)
  (cond ((= i j k) 0)
        ((= i j) (num* i k k))
        (t (+ (tet (- k 2)) (tri (- j 2)) i))))

(defun num (triple)
  "convert throw of three dice into number from 0 to 35 uniformly"
  (apply #'num* (sort triple #'<)))

(defun topair (triple)
    "convert throw of three dice into throw of two dice uniformly"
    (multiple-value-bind (q r) (floor (num triple) 6)
      (list (+ q 1) (+ r 1))))

(defun test ()
  (let ((c (make-array '(6 6) :initial-element 0)))
    (loop for i from 1 to 6 do
         (loop for j from 1 to 6 do
              (loop for k from 1 to 6
                 for (a b) = (topair (list i j k)) do
                   (incf (aref c (- a 1) (- b 1))))))
    c))
