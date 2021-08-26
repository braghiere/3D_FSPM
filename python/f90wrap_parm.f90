! Module parm defined in file ../src/parm.f

subroutine f90wrap_polanyi_initialise(this)
    use parm, only: polanyi
    implicit none
    
    type polanyi_ptr_type
        type(polanyi), pointer :: p => NULL()
    end type polanyi_ptr_type
    type(polanyi_ptr_type) :: this_ptr
    integer, intent(out), dimension(2) :: this
    allocate(this_ptr%p)
    this = transfer(this_ptr, this)
end subroutine f90wrap_polanyi_initialise

subroutine f90wrap_polanyi_finalise(this)
    use parm, only: polanyi
    implicit none
    
    type polanyi_ptr_type
        type(polanyi), pointer :: p => NULL()
    end type polanyi_ptr_type
    type(polanyi_ptr_type) :: this_ptr
    integer, intent(in), dimension(2) :: this
    this_ptr = transfer(this, this_ptr)
    deallocate(this_ptr%p)
end subroutine f90wrap_polanyi_finalise

subroutine f90wrap_parm__get__type_i4(f90wrap_type_i4)
    use parm, only: parm_type_i4 => type_i4
    implicit none
    integer, intent(out) :: f90wrap_type_i4
    
    f90wrap_type_i4 = parm_type_i4
end subroutine f90wrap_parm__get__type_i4

subroutine f90wrap_parm__get__type_i2(f90wrap_type_i2)
    use parm, only: parm_type_i2 => type_i2
    implicit none
    integer, intent(out) :: f90wrap_type_i2
    
    f90wrap_type_i2 = parm_type_i2
end subroutine f90wrap_parm__get__type_i2

subroutine f90wrap_parm__get__type_i1(f90wrap_type_i1)
    use parm, only: parm_type_i1 => type_i1
    implicit none
    integer, intent(out) :: f90wrap_type_i1
    
    f90wrap_type_i1 = parm_type_i1
end subroutine f90wrap_parm__get__type_i1

subroutine f90wrap_parm__get__type_r4(f90wrap_type_r4)
    use parm, only: parm_type_r4 => type_r4
    implicit none
    integer, intent(out) :: f90wrap_type_r4
    
    f90wrap_type_r4 = parm_type_r4
end subroutine f90wrap_parm__get__type_r4

subroutine f90wrap_parm__get__type_r8(f90wrap_type_r8)
    use parm, only: parm_type_r8 => type_r8
    implicit none
    integer, intent(out) :: f90wrap_type_r8
    
    f90wrap_type_r8 = parm_type_r8
end subroutine f90wrap_parm__get__type_r8

subroutine f90wrap_parm__get__ncon(f90wrap_ncon)
    use parm, only: parm_ncon => ncon
    implicit none
    integer(4), intent(out) :: f90wrap_ncon
    
    f90wrap_ncon = parm_ncon
end subroutine f90wrap_parm__get__ncon

subroutine f90wrap_parm__get__maxndr(f90wrap_maxndr)
    use parm, only: parm_maxndr => maxndr
    implicit none
    integer(4), intent(out) :: f90wrap_maxndr
    
    f90wrap_maxndr = parm_maxndr
end subroutine f90wrap_parm__get__maxndr

subroutine f90wrap_parm__get__maxnpr(f90wrap_maxnpr)
    use parm, only: parm_maxnpr => maxnpr
    implicit none
    integer(4), intent(out) :: f90wrap_maxnpr
    
    f90wrap_maxnpr = parm_maxnpr
end subroutine f90wrap_parm__get__maxnpr

subroutine f90wrap_parm__get__maxnrc(f90wrap_maxnrc)
    use parm, only: parm_maxnrc => maxnrc
    implicit none
    integer(4), intent(out) :: f90wrap_maxnrc
    
    f90wrap_maxnrc = parm_maxnrc
end subroutine f90wrap_parm__get__maxnrc

subroutine f90wrap_parm__get__maxnor(f90wrap_maxnor)
    use parm, only: parm_maxnor => maxnor
    implicit none
    integer(4), intent(out) :: f90wrap_maxnor
    
    f90wrap_maxnor = parm_maxnor
end subroutine f90wrap_parm__get__maxnor

! End of module parm defined in file ../src/parm.f

