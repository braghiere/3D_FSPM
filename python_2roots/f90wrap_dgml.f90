! Module dgml defined in file ../src/dgml.f

subroutine f90wrap_dgml__get__dgm(f90wrap_dgm)
    use dgml, only: dgml_dgm => dgm
    implicit none
    logical, intent(out) :: f90wrap_dgm
    
    f90wrap_dgm = dgml_dgm
end subroutine f90wrap_dgml__get__dgm

subroutine f90wrap_dgml__set__dgm(f90wrap_dgm)
    use dgml, only: dgml_dgm => dgm
    implicit none
    logical, intent(in) :: f90wrap_dgm
    
    dgml_dgm = f90wrap_dgm
end subroutine f90wrap_dgml__set__dgm

subroutine f90wrap_dgml__get__maxwell(f90wrap_maxwell)
    use dgml, only: dgml_maxwell => maxwell
    implicit none
    logical, intent(out) :: f90wrap_maxwell
    
    f90wrap_maxwell = dgml_maxwell
end subroutine f90wrap_dgml__get__maxwell

subroutine f90wrap_dgml__set__maxwell(f90wrap_maxwell)
    use dgml, only: dgml_maxwell => maxwell
    implicit none
    logical, intent(in) :: f90wrap_maxwell
    
    dgml_maxwell = f90wrap_maxwell
end subroutine f90wrap_dgml__set__maxwell

subroutine f90wrap_dgml__get__equimolar(f90wrap_equimolar)
    use dgml, only: dgml_equimolar => equimolar
    implicit none
    logical, intent(out) :: f90wrap_equimolar
    
    f90wrap_equimolar = dgml_equimolar
end subroutine f90wrap_dgml__get__equimolar

subroutine f90wrap_dgml__set__equimolar(f90wrap_equimolar)
    use dgml, only: dgml_equimolar => equimolar
    implicit none
    logical, intent(in) :: f90wrap_equimolar
    
    dgml_equimolar = f90wrap_equimolar
end subroutine f90wrap_dgml__set__equimolar

! End of module dgml defined in file ../src/dgml.f

