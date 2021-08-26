subroutine f90wrap_alkcalc(alk_carb, alk_noncarb, alk_tot, alk_carb_mg, &
    alk_noncarb_mg, alk_tot_mg, alkfacc, alkfacx, c, cx, iax, jax, nc, nx, &
    namec, namex)
    implicit none
    external alkcalc
    
    real :: alk_carb
    !f2py intent(inout) alk_carb
    real :: alk_noncarb
    !f2py intent(inout) alk_noncarb
    real :: alk_tot
    !f2py intent(inout) alk_tot
    real :: alk_carb_mg
    !f2py intent(inout) alk_carb_mg
    real :: alk_noncarb_mg
    !f2py intent(inout) alk_noncarb_mg
    real :: alk_tot_mg
    !f2py intent(inout) alk_tot_mg
    real :: alkfacc
    !f2py intent(inout) alkfacc
    real :: alkfacx
    !f2py intent(inout) alkfacx
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    integer :: iax
    !f2py intent(inout) iax
    integer :: jax
    !f2py intent(inout) jax
    integer :: nc
    !f2py intent(inout) nc
    integer :: nx
    !f2py intent(inout) nx
    integer :: namec
    !f2py intent(inout) namec
    integer :: namex
    !f2py intent(inout) namex
    call alkcalc(alk_carb, alk_noncarb, alk_tot, alk_carb_mg, alk_noncarb_mg, &
        alk_tot_mg, alkfacc, alkfacx, c, cx, iax, jax, nc, nx, namec, namex)
end subroutine f90wrap_alkcalc

subroutine f90wrap_alpha(im, ivol)
    implicit none
    external alpha
    
    integer :: im
    !f2py intent(inout) im
    integer :: ivol
    !f2py intent(inout) ivol
    call alpha(im, ivol)
end subroutine f90wrap_alpha

subroutine f90wrap_dalpha(im, ivol)
    implicit none
    external dalpha
    
    integer :: im
    !f2py intent(inout) im
    integer :: ivol
    !f2py intent(inout) ivol
    call dalpha(im, ivol)
end subroutine f90wrap_dalpha

subroutine f90wrap_andorra(nsb, component_type, iasb, jasb, nc, cnew, csb, &
    nelec, nsites, namesb, namec, sorption_group, chargesb, xnusb, nsites2, &
    chargec, sorption_type, cap1, cap2, site_mass, site_area, totpsi, calcpsi, &
    strionsb, surfacensb)
    implicit none
    external andorra
    
    integer :: nsb
    !f2py intent(inout) nsb
    real :: component_type
    !f2py intent(inout) component_type
    integer :: iasb
    !f2py intent(inout) iasb
    integer :: jasb
    !f2py intent(inout) jasb
    integer :: nc
    !f2py intent(inout) nc
    real :: cnew
    !f2py intent(inout) cnew
    real :: csb
    !f2py intent(inout) csb
    integer :: nelec
    !f2py intent(inout) nelec
    integer :: nsites
    !f2py intent(inout) nsites
    integer :: namesb
    !f2py intent(inout) namesb
    integer :: namec
    !f2py intent(inout) namec
    real :: sorption_group
    !f2py intent(inout) sorption_group
    real :: chargesb
    !f2py intent(inout) chargesb
    real :: xnusb
    !f2py intent(inout) xnusb
    integer :: nsites2
    !f2py intent(inout) nsites2
    real :: chargec
    !f2py intent(inout) chargec
    real :: sorption_type
    !f2py intent(inout) sorption_type
    real :: cap1
    !f2py intent(inout) cap1
    real :: cap2
    !f2py intent(inout) cap2
    real :: site_mass
    !f2py intent(inout) site_mass
    real :: site_area
    !f2py intent(inout) site_area
    real :: totpsi
    !f2py intent(inout) totpsi
    real :: calcpsi
    !f2py intent(inout) calcpsi
    real :: strionsb
    !f2py intent(inout) strionsb
    real :: surfacensb
    !f2py intent(inout) surfacensb
    call andorra(nsb, component_type, iasb, jasb, nc, cnew, csb, nelec, nsites, &
        namesb, namec, sorption_group, chargesb, xnusb, nsites2, chargec, &
        sorption_type, cap1, cap2, site_mass, site_area, totpsi, calcpsi, strionsb, &
        surfacensb)
end subroutine f90wrap_andorra

subroutine f90wrap_aratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, &
    aream, im, jbl, ivol)
    implicit none
    external aratemin
    
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: ratem
    !f2py intent(inout) ratem
    real :: phim
    !f2py intent(inout) phim
    real :: phimold
    !f2py intent(inout) phimold
    real :: aream
    !f2py intent(inout) aream
    integer :: im
    !f2py intent(inout) im
    integer :: jbl
    !f2py intent(inout) jbl
    integer :: ivol
    !f2py intent(inout) ivol
    call aratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, im, jbl, &
        ivol)
end subroutine f90wrap_aratemin

subroutine f90wrap_atotconc(c, cx, jbl)
    implicit none
    external atotconc
    
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    integer :: jbl
    !f2py intent(inout) jbl
    call atotconc(c, cx, jbl)
end subroutine f90wrap_atotconc

subroutine f90wrap_batreac
    implicit none
    external batreac
    
    call batreac()
end subroutine f90wrap_batreac

subroutine f90wrap_binmatevap
    implicit none
    external binmatevap
    
    call binmatevap()
end subroutine f90wrap_binmatevap

subroutine f90wrap_binmattransp
    implicit none
    external binmattransp
    
    call binmattransp()
end subroutine f90wrap_binmattransp

subroutine f90wrap_cbalance(c, cx, zbal, zpos, zneg)
    implicit none
    external cbalance
    
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: zbal
    !f2py intent(inout) zbal
    real :: zpos
    !f2py intent(inout) zpos
    real :: zneg
    !f2py intent(inout) zneg
    call cbalance(c, cx, zbal, zpos, zneg)
end subroutine f90wrap_cbalance

subroutine f90wrap_checkerr(ierr, label, ilog)
    implicit none
    external checkerr
    
    integer :: ierr
    !f2py intent(inout) ierr
    character(*) :: label
    !f2py intent(inout) label
    integer :: ilog
    !f2py intent(inout) ilog
    call checkerr(ierr, label, ilog)
end subroutine f90wrap_checkerr

subroutine f90wrap_checksat
    implicit none
    external checksat
    
    call checksat()
end subroutine f90wrap_checksat

subroutine f90wrap_chrgcorr
    implicit none
    external chrgcorr
    
    call chrgcorr()
end subroutine f90wrap_chrgcorr

subroutine f90wrap_cliqdisp(nx, ny, nz, ix, iy, iz, fvpair, npair, aread, d, &
    half_cells, nmax, idbg, dd)
    implicit none
    external cliqdisp
    
    integer :: nx
    !f2py intent(inout) nx
    integer :: ny
    !f2py intent(inout) ny
    integer :: nz
    !f2py intent(inout) nz
    integer :: ix
    !f2py intent(inout) ix
    integer :: iy
    !f2py intent(inout) iy
    integer :: iz
    !f2py intent(inout) iz
    integer, dimension(3,12,2) :: fvpair
    !f2py intent(inout) fvpair
    integer, dimension(3) :: npair
    !f2py intent(inout) npair
    real :: aread
    !f2py intent(inout) aread
    real :: d
    !f2py intent(inout) d
    logical :: half_cells
    !f2py intent(inout) half_cells
    integer :: nmax
    !f2py intent(inout) nmax
    integer :: idbg
    !f2py intent(inout) idbg
    real :: dd
    !f2py intent(inout) dd
    call cliqdisp(nx, ny, nz, ix, iy, iz, fvpair, npair, aread, d, half_cells, nmax, &
        idbg, dd)
end subroutine f90wrap_cliqdisp

subroutine f90wrap_clsgfls
    implicit none
    external clsgfls
    
    call clsgfls()
end subroutine f90wrap_clsgfls

subroutine f90wrap_clstpfls
    implicit none
    external clstpfls
    
    call clstpfls()
end subroutine f90wrap_clstpfls

subroutine f90wrap_comptotc(totc)
    implicit none
    external comptotc
    
    real :: totc
    !f2py intent(inout) totc
    call comptotc(totc)
end subroutine f90wrap_comptotc

subroutine f90wrap_concsort(conc, gamma, name, n)
    implicit none
    external concsort
    
    real :: conc
    !f2py intent(inout) conc
    real :: gamma
    !f2py intent(inout) gamma
    integer :: name
    !f2py intent(inout) name
    integer :: n
    !f2py intent(inout) n
    call concsort(conc, gamma, name, n)
end subroutine f90wrap_concsort

subroutine f90wrap_constnts
    implicit none
    external constnts
    
    call constnts()
end subroutine f90wrap_constnts

subroutine f90wrap_cvolume
    implicit none
    external cvolume
    
    call cvolume()
end subroutine f90wrap_cvolume

subroutine f90wrap_dandorra(nsb, component_type, iasb, jasb, nc, cnew, dcsb, &
    nelec, nsites, namesb, namec, sorption_group, chargesb, xnusb, nsites2, &
    chargec, sorption_type, cap1, cap2, site_mass, site_area, dtotpsi, dcalcpsi, &
    strionsb, surfacensb, cinc, drtinc)
    implicit none
    external dandorra
    
    integer :: nsb
    !f2py intent(inout) nsb
    real :: component_type
    !f2py intent(inout) component_type
    integer :: iasb
    !f2py intent(inout) iasb
    integer :: jasb
    !f2py intent(inout) jasb
    integer :: nc
    !f2py intent(inout) nc
    real :: cnew
    !f2py intent(inout) cnew
    real :: dcsb
    !f2py intent(inout) dcsb
    integer :: nelec
    !f2py intent(inout) nelec
    integer :: nsites
    !f2py intent(inout) nsites
    integer :: namesb
    !f2py intent(inout) namesb
    integer :: namec
    !f2py intent(inout) namec
    real :: sorption_group
    !f2py intent(inout) sorption_group
    real :: chargesb
    !f2py intent(inout) chargesb
    real :: xnusb
    !f2py intent(inout) xnusb
    integer :: nsites2
    !f2py intent(inout) nsites2
    real :: chargec
    !f2py intent(inout) chargec
    real :: sorption_type
    !f2py intent(inout) sorption_type
    real :: cap1
    !f2py intent(inout) cap1
    real :: cap2
    !f2py intent(inout) cap2
    real :: site_mass
    !f2py intent(inout) site_mass
    real :: site_area
    !f2py intent(inout) site_area
    real :: dtotpsi
    !f2py intent(inout) dtotpsi
    real :: dcalcpsi
    !f2py intent(inout) dcalcpsi
    real :: strionsb
    !f2py intent(inout) strionsb
    real :: surfacensb
    !f2py intent(inout) surfacensb
    real :: cinc
    !f2py intent(inout) cinc
    real :: drtinc
    !f2py intent(inout) drtinc
    call dandorra(nsb, component_type, iasb, jasb, nc, cnew, dcsb, nelec, nsites, &
        namesb, namec, sorption_group, chargesb, xnusb, nsites2, chargec, &
        sorption_type, cap1, cap2, site_mass, site_area, dtotpsi, dcalcpsi, &
        strionsb, surfacensb, cinc, drtinc)
end subroutine f90wrap_dandorra

subroutine f90wrap_datstr_1
    implicit none
    external datstr_1
    
    call datstr_1()
end subroutine f90wrap_datstr_1

subroutine f90wrap_datstr_n
    implicit none
    external datstr_n
    
    call datstr_n()
end subroutine f90wrap_datstr_n

subroutine f90wrap_dgefam(a, lda, n, ipvt, info, n0, n1, n2)
    implicit none
    external dgefam
    
    double precision, dimension(n0,n1) :: a
    !f2py intent(inout) a
    integer :: lda
    !f2py intent(inout) lda
    integer :: n
    !f2py intent(inout) n
    integer, dimension(n2) :: ipvt
    !f2py intent(inout) ipvt
    integer :: info
    !f2py intent(inout) info
    integer :: n0
    !f2py intent(hide), depend(a) :: n0 = shape(a,0)
    integer :: n1
    !f2py intent(hide), depend(a) :: n1 = shape(a,1)
    integer :: n2
    !f2py intent(hide), depend(ipvt) :: n2 = shape(ipvt,0)
    call dgefam(a, lda, n, ipvt, info)
end subroutine f90wrap_dgefam

subroutine f90wrap_dgeslm(a, lda, n, ipvt, b, n0, n1, n2, n3)
    implicit none
    external dgeslm
    
    double precision, dimension(n0,n1) :: a
    !f2py intent(inout) a
    integer :: lda
    !f2py intent(inout) lda
    integer :: n
    !f2py intent(inout) n
    integer, dimension(n2) :: ipvt
    !f2py intent(inout) ipvt
    double precision, dimension(n3) :: b
    !f2py intent(inout) b
    integer :: n0
    !f2py intent(hide), depend(a) :: n0 = shape(a,0)
    integer :: n1
    !f2py intent(hide), depend(a) :: n1 = shape(a,1)
    integer :: n2
    !f2py intent(hide), depend(ipvt) :: n2 = shape(ipvt,0)
    integer :: n3
    !f2py intent(hide), depend(b) :: n3 = shape(b,0)
    call dgeslm(a, lda, n, ipvt, b)
end subroutine f90wrap_dgeslm

subroutine f90wrap_dgm_dfluxdg(c_i, c_j, dc_i, dmolfrac_i, zgi, zgj, dens, gpij, &
    tempkel, relp, tauijx, gporx, delta_ijx, small, factor, ipvt, ludecomp, &
    fmat, dgm_dgflux)
    implicit none
    external dgm_dfluxdg
    
    real :: c_i
    !f2py intent(inout) c_i
    real :: c_j
    !f2py intent(inout) c_j
    real :: dc_i
    !f2py intent(inout) dc_i
    real :: dmolfrac_i
    !f2py intent(inout) dmolfrac_i
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: dens
    !f2py intent(inout) dens
    real :: gpij
    !f2py intent(inout) gpij
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: relp
    !f2py intent(inout) relp
    real :: tauijx
    !f2py intent(inout) tauijx
    real :: gporx
    !f2py intent(inout) gporx
    real :: delta_ijx
    !f2py intent(inout) delta_ijx
    real :: small
    !f2py intent(inout) small
    real :: factor
    !f2py intent(inout) factor
    integer :: ipvt
    !f2py intent(inout) ipvt
    integer :: ludecomp
    !f2py intent(inout) ludecomp
    real :: fmat
    !f2py intent(inout) fmat
    real :: dgm_dgflux
    !f2py intent(inout) dgm_dgflux
    call dgm_dfluxdg(c_i, c_j, dc_i, dmolfrac_i, zgi, zgj, dens, gpij, tempkel, &
        relp, tauijx, gporx, delta_ijx, small, factor, ipvt, ludecomp, fmat, &
        dgm_dgflux)
end subroutine f90wrap_dgm_dfluxdg

subroutine f90wrap_dgm_fluxdg(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, &
    tempkel, permijy, relp, tauijx, gporx, delta_ijx, small, amat, bmat, ipvt, &
    dgm_gflux, dgm_neflux)
    implicit none
    external dgm_fluxdg
    
    real :: c_i
    !f2py intent(inout) c_i
    real :: c_j
    !f2py intent(inout) c_j
    real :: c_ij
    !f2py intent(inout) c_ij
    integer :: molfrac
    !f2py intent(inout) molfrac
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: dens
    !f2py intent(inout) dens
    real :: gpij
    !f2py intent(inout) gpij
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: permijy
    !f2py intent(inout) permijy
    real :: relp
    !f2py intent(inout) relp
    real :: tauijx
    !f2py intent(inout) tauijx
    real :: gporx
    !f2py intent(inout) gporx
    real :: delta_ijx
    !f2py intent(inout) delta_ijx
    real :: small
    !f2py intent(inout) small
    real :: amat
    !f2py intent(inout) amat
    real :: bmat
    !f2py intent(inout) bmat
    integer :: ipvt
    !f2py intent(inout) ipvt
    real :: dgm_gflux
    !f2py intent(inout) dgm_gflux
    real :: dgm_neflux
    !f2py intent(inout) dgm_neflux
    call dgm_fluxdg(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, permijy, &
        relp, tauijx, gporx, delta_ijx, small, amat, bmat, ipvt, dgm_gflux, &
        dgm_neflux)
end subroutine f90wrap_dgm_fluxdg

subroutine f90wrap_dgm_fluxdg_s(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, &
    tempkel, permijy, relp, tauijx, gporx, delta_ijx, small, amat, bmat, ipvt, &
    dgm_gflux_s, dgm_neflux_s)
    implicit none
    external dgm_fluxdg_s
    
    real :: c_i
    !f2py intent(inout) c_i
    real :: c_j
    !f2py intent(inout) c_j
    real :: c_ij
    !f2py intent(inout) c_ij
    integer :: molfrac
    !f2py intent(inout) molfrac
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: dens
    !f2py intent(inout) dens
    real :: gpij
    !f2py intent(inout) gpij
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: permijy
    !f2py intent(inout) permijy
    real :: relp
    !f2py intent(inout) relp
    real :: tauijx
    !f2py intent(inout) tauijx
    real :: gporx
    !f2py intent(inout) gporx
    real :: delta_ijx
    !f2py intent(inout) delta_ijx
    real :: small
    !f2py intent(inout) small
    real :: amat
    !f2py intent(inout) amat
    real :: bmat
    !f2py intent(inout) bmat
    integer :: ipvt
    !f2py intent(inout) ipvt
    real :: dgm_gflux_s
    !f2py intent(inout) dgm_gflux_s
    real :: dgm_neflux_s
    !f2py intent(inout) dgm_neflux_s
    call dgm_fluxdg_s(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, &
        permijy, relp, tauijx, gporx, delta_ijx, small, amat, bmat, ipvt, &
        dgm_gflux_s, dgm_neflux_s)
end subroutine f90wrap_dgm_fluxdg_s

subroutine f90wrap_dhconst(dhad, dhbd, tempk, tconv)
    implicit none
    external dhconst
    
    real :: dhad
    !f2py intent(inout) dhad
    real :: dhbd
    !f2py intent(inout) dhbd
    real :: tempk
    !f2py intent(inout) tempk
    real :: tconv
    !f2py intent(inout) tconv
    call dhconst(dhad, dhbd, tempk, tconv)
end subroutine f90wrap_dhconst

subroutine f90wrap_diff_grad(c_i, c_j, molfrac, zgi, zgj, dens, tempkel, gporx, &
    delta_ijx, grad_diff)
    implicit none
    external diff_grad
    
    real :: c_i
    !f2py intent(inout) c_i
    real :: c_j
    !f2py intent(inout) c_j
    integer :: molfrac
    !f2py intent(inout) molfrac
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: dens
    !f2py intent(inout) dens
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: gporx
    !f2py intent(inout) gporx
    real :: delta_ijx
    !f2py intent(inout) delta_ijx
    real :: grad_diff
    !f2py intent(inout) grad_diff
    call diff_grad(c_i, c_j, molfrac, zgi, zgj, dens, tempkel, gporx, delta_ijx, &
        grad_diff)
end subroutine f90wrap_diff_grad

subroutine f90wrap_distmp(cmnewm, phim, aream)
    implicit none
    external distmp
    
    real :: cmnewm
    !f2py intent(inout) cmnewm
    real :: phim
    !f2py intent(inout) phim
    real :: aream
    !f2py intent(inout) aream
    call distmp(cmnewm, phim, aream)
end subroutine f90wrap_distmp

subroutine f90wrap_draoult(c, gammac, ratem, phim, phimold, aream, drtinc, im)
    implicit none
    external draoult
    
    real :: c
    !f2py intent(inout) c
    real :: gammac
    !f2py intent(inout) gammac
    real :: ratem
    !f2py intent(inout) ratem
    real :: phim
    !f2py intent(inout) phim
    real :: phimold
    !f2py intent(inout) phimold
    real :: aream
    !f2py intent(inout) aream
    real :: drtinc
    !f2py intent(inout) drtinc
    integer :: im
    !f2py intent(inout) im
    call draoult(c, gammac, ratem, phim, phimold, aream, drtinc, im)
end subroutine f90wrap_draoult

subroutine f90wrap_drategas(g, tkel, hhead, zg, drtinc)
    implicit none
    external drategas
    
    real :: g
    !f2py intent(inout) g
    real :: tkel
    !f2py intent(inout) tkel
    real :: hhead
    !f2py intent(inout) hhead
    real :: zg
    !f2py intent(inout) zg
    real :: drtinc
    !f2py intent(inout) drtinc
    call drategas(g, tkel, hhead, zg, drtinc)
end subroutine f90wrap_drategas

subroutine f90wrap_drateint(rate, totc, c, gammac, phim, drtinc, iaq)
    implicit none
    external drateint
    
    real :: rate
    !f2py intent(inout) rate
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: gammac
    !f2py intent(inout) gammac
    real :: phim
    !f2py intent(inout) phim
    real :: drtinc
    !f2py intent(inout) drtinc
    integer :: iaq
    !f2py intent(inout) iaq
    call drateint(rate, totc, c, gammac, phim, drtinc, iaq)
end subroutine f90wrap_drateint

subroutine f90wrap_drateint_new(rate, totc, c, cx, gammac, gammax, phim, drtinc, &
    iaq, sw, por, rootdens, wrf)
    implicit none
    external drateint_new
    
    real :: rate
    !f2py intent(inout) rate
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: phim
    !f2py intent(inout) phim
    real :: drtinc
    !f2py intent(inout) drtinc
    integer :: iaq
    !f2py intent(inout) iaq
    real :: sw
    !f2py intent(inout) sw
    real :: por
    !f2py intent(inout) por
    real :: rootdens
    !f2py intent(inout) rootdens
    real :: wrf
    !f2py intent(inout) wrf
    call drateint_new(rate, totc, c, cx, gammac, gammax, phim, drtinc, iaq, sw, por, &
        rootdens, wrf)
end subroutine f90wrap_drateint_new

subroutine f90wrap_dratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, &
    aream, drtinc, im, ivol)
    implicit none
    external dratemin
    
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: ratem
    !f2py intent(inout) ratem
    real :: phim
    !f2py intent(inout) phim
    real :: phimold
    !f2py intent(inout) phimold
    real :: aream
    !f2py intent(inout) aream
    real :: drtinc
    !f2py intent(inout) drtinc
    integer :: im
    !f2py intent(inout) im
    integer :: ivol
    !f2py intent(inout) ivol
    call dratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, drtinc, &
        im, ivol)
end subroutine f90wrap_dratemin

subroutine f90wrap_dratemin_new(totc, c, cx, gammac, gammax, ratem, phim, &
    phimold, aream, drtinc, im, ivol, sw, por, rootdens, rootdens2)
    implicit none
    external dratemin_new
    
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: ratem
    !f2py intent(inout) ratem
    real :: phim
    !f2py intent(inout) phim
    real :: phimold
    !f2py intent(inout) phimold
    real :: aream
    !f2py intent(inout) aream
    real :: drtinc
    !f2py intent(inout) drtinc
    integer :: im
    !f2py intent(inout) im
    integer :: ivol
    !f2py intent(inout) ivol
    real :: sw
    !f2py intent(inout) sw
    real :: por
    !f2py intent(inout) por
    real :: rootdens
    !f2py intent(inout) rootdens
    real :: rootdens2
    !f2py intent(inout) rootdens2
    call dratemin_new(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, &
        drtinc, im, ivol, sw, por, rootdens, rootdens2)
end subroutine f90wrap_dratemin_new

subroutine f90wrap_draterdx(c, cx, gammac, gammax, drate, totc, drtinc, ir, &
    idbg)
    implicit none
    external draterdx
    
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: drate
    !f2py intent(inout) drate
    real :: totc
    !f2py intent(inout) totc
    real :: drtinc
    !f2py intent(inout) drtinc
    integer :: ir
    !f2py intent(inout) ir
    integer :: idbg
    !f2py intent(inout) idbg
    call draterdx(c, cx, gammac, gammax, drate, totc, drtinc, ir, idbg)
end subroutine f90wrap_draterdx

subroutine f90wrap_dsorbspc(dcsb, cec, eqsb, gammac, c, xnusb, iasb, jasb, nsb, &
    isb, kc)
    implicit none
    external dsorbspc
    
    real :: dcsb
    !f2py intent(inout) dcsb
    real :: cec
    !f2py intent(inout) cec
    real :: eqsb
    !f2py intent(inout) eqsb
    real :: gammac
    !f2py intent(inout) gammac
    real :: c
    !f2py intent(inout) c
    real :: xnusb
    !f2py intent(inout) xnusb
    integer :: iasb
    !f2py intent(inout) iasb
    integer :: jasb
    !f2py intent(inout) jasb
    integer :: nsb
    !f2py intent(inout) nsb
    integer :: isb
    !f2py intent(inout) isb
    integer :: kc
    !f2py intent(inout) kc
    call dsorbspc(dcsb, cec, eqsb, gammac, c, xnusb, iasb, jasb, nsb, isb, kc)
end subroutine f90wrap_dsorbspc

subroutine f90wrap_dtotconc(c, cx, drtinc, jbl)
    implicit none
    external dtotconc
    
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: drtinc
    !f2py intent(inout) drtinc
    integer :: jbl
    !f2py intent(inout) jbl
    call dtotconc(c, cx, drtinc, jbl)
end subroutine f90wrap_dtotconc

subroutine f90wrap_dtotcong(g, ginc, dtotg, xnug, drtinc, iaga, jaga, nc, ng, &
    jbl, namec)
    implicit none
    external dtotcong
    
    real :: g
    !f2py intent(inout) g
    real :: ginc
    !f2py intent(inout) ginc
    real :: dtotg
    !f2py intent(inout) dtotg
    real :: xnug
    !f2py intent(inout) xnug
    real :: drtinc
    !f2py intent(inout) drtinc
    integer :: iaga
    !f2py intent(inout) iaga
    integer :: jaga
    !f2py intent(inout) jaga
    integer :: nc
    !f2py intent(inout) nc
    integer :: ng
    !f2py intent(inout) ng
    integer :: jbl
    !f2py intent(inout) jbl
    integer :: namec
    !f2py intent(inout) namec
    call dtotcong(g, ginc, dtotg, xnug, drtinc, iaga, jaga, nc, ng, jbl, namec)
end subroutine f90wrap_dtotcong

subroutine f90wrap_findkey(keyword1, keyword2, itmp, found_keyword, searching)
    implicit none
    external findkey
    
    integer :: keyword1
    !f2py intent(inout) keyword1
    integer :: keyword2
    !f2py intent(inout) keyword2
    integer :: itmp
    !f2py intent(inout) itmp
    logical :: found_keyword
    !f2py intent(inout) found_keyword
    logical :: searching
    !f2py intent(inout) searching
    call findkey(keyword1, keyword2, itmp, found_keyword, searching)
end subroutine f90wrap_findkey

subroutine f90wrap_findname(name, itmp, found_name)
    implicit none
    external findname
    
    integer :: name
    !f2py intent(inout) name
    integer :: itmp
    !f2py intent(inout) itmp
    logical :: found_name
    !f2py intent(inout) found_name
    call findname(name, itmp, found_name)
end subroutine f90wrap_findname

subroutine f90wrap_findpath(ipath, im)
    implicit none
    external findpath
    
    integer :: ipath
    !f2py intent(inout) ipath
    integer :: im
    !f2py intent(inout) im
    call findpath(ipath, im)
end subroutine f90wrap_findpath

subroutine f90wrap_findstrg(subsection, itmp, found_subsection)
    implicit none
    external findstrg
    
    real :: subsection
    !f2py intent(inout) subsection
    integer :: itmp
    !f2py intent(inout) itmp
    logical :: found_subsection
    !f2py intent(inout) found_subsection
    call findstrg(subsection, itmp, found_subsection)
end subroutine f90wrap_findstrg

subroutine f90wrap_findvol(veln, x, y, z)
    implicit none
    external findvol
    
    integer(4) :: veln
    !f2py intent(inout) veln
    real :: x
    !f2py intent(inout) x
    real :: y
    !f2py intent(inout) y
    real :: z
    !f2py intent(inout) z
    call findvol(veln, x, y, z)
end subroutine f90wrap_findvol

subroutine f90wrap_findzone(subsection, itmp, found_subsection, izone, &
    zone_name)
    implicit none
    external findzone
    
    real :: subsection
    !f2py intent(inout) subsection
    integer :: itmp
    !f2py intent(inout) itmp
    logical :: found_subsection
    !f2py intent(inout) found_subsection
    integer :: izone
    !f2py intent(inout) izone
    real :: zone_name
    !f2py intent(inout) zone_name
    call findzone(subsection, itmp, found_subsection, izone, zone_name)
end subroutine f90wrap_findzone

subroutine f90wrap_fsflow
    implicit none
    external fsflow
    
    call fsflow()
end subroutine f90wrap_fsflow

subroutine f90wrap_gasconc(c, gammac, g, ig, tempkel)
    implicit none
    external gasconc
    
    real :: c
    !f2py intent(inout) c
    real :: gammac
    !f2py intent(inout) gammac
    real :: g
    !f2py intent(inout) g
    integer :: ig
    !f2py intent(inout) ig
    real :: tempkel
    !f2py intent(inout) tempkel
    call gasconc(c, gammac, g, ig, tempkel)
end subroutine f90wrap_gasconc

subroutine f90wrap_gcconst
    implicit none
    external gcconst
    
    call gcconst()
end subroutine f90wrap_gcconst

subroutine f90wrap_gcreact(cnew, cold, cx, gammac, gammax, gnew, sw, sa, por, &
    igen, ilog, idbg, tec_header, prefix, l_prfx, zone_name, l_zone_name)
    implicit none
    external gcreact
    
    real :: cnew
    !f2py intent(inout) cnew
    real :: cold
    !f2py intent(inout) cold
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: gnew
    !f2py intent(inout) gnew
    real :: sw
    !f2py intent(inout) sw
    real :: sa
    !f2py intent(inout) sa
    real :: por
    !f2py intent(inout) por
    integer :: igen
    !f2py intent(inout) igen
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    logical :: tec_header
    !f2py intent(inout) tec_header
    real :: prefix
    !f2py intent(inout) prefix
    integer :: l_prfx
    !f2py intent(inout) l_prfx
    real :: zone_name
    !f2py intent(inout) zone_name
    integer :: l_zone_name
    !f2py intent(inout) l_zone_name
    call gcreact(cnew, cold, cx, gammac, gammax, gnew, sw, sa, por, igen, ilog, &
        idbg, tec_header, prefix, l_prfx, zone_name, l_zone_name)
end subroutine f90wrap_gcreact

subroutine f90wrap_get_gam(ivol, gam, inc, diag, gamcon)
    implicit none
    external get_gam
    
    integer :: ivol
    !f2py intent(inout) ivol
    real :: gam
    !f2py intent(inout) gam
    logical :: inc
    !f2py intent(inout) inc
    logical :: diag
    !f2py intent(inout) diag
    real :: gamcon
    !f2py intent(inout) gamcon
    call get_gam(ivol, gam, inc, diag, gamcon)
end subroutine f90wrap_get_gam

subroutine f90wrap_giups
    implicit none
    external giups
    
    call giups()
end subroutine f90wrap_giups

subroutine f90wrap_giups_brt(gpi, gpj, zgi, zgj, dens_i, dens_j, jbrt)
    implicit none
    external giups_brt
    
    real :: gpi
    !f2py intent(inout) gpi
    real :: gpj
    !f2py intent(inout) gpj
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: dens_i
    !f2py intent(inout) dens_i
    real :: dens_j
    !f2py intent(inout) dens_j
    integer :: jbrt
    !f2py intent(inout) jbrt
    call giups_brt(gpi, gpj, zgi, zgj, dens_i, dens_j, jbrt)
end subroutine f90wrap_giups_brt

subroutine f90wrap_guess(cnew, cold, tempkel, ilog)
    implicit none
    external guess
    
    real :: cnew
    !f2py intent(inout) cnew
    real :: cold
    !f2py intent(inout) cold
    real :: tempkel
    !f2py intent(inout) tempkel
    integer :: ilog
    !f2py intent(inout) ilog
    call guess(cnew, cold, tempkel, ilog)
end subroutine f90wrap_guess

subroutine f90wrap_i2upfind
    implicit none
    external i2upfind
    
    call i2upfind()
end subroutine f90wrap_i2upfind

subroutine f90wrap_iajabl
    implicit none
    external iajabl
    
    call iajabl()
end subroutine f90wrap_iajabl

subroutine f90wrap_iajart
    implicit none
    external iajart
    
    call iajart()
end subroutine f90wrap_iajart

subroutine f90wrap_iajavs
    implicit none
    external iajavs
    
    call iajavs()
end subroutine f90wrap_iajavs

subroutine f90wrap_iajavs_dp
    implicit none
    external iajavs_dp
    
    call iajavs_dp()
end subroutine f90wrap_iajavs_dp

subroutine f90wrap_icbcrt(ivol, imin)
    implicit none
    external icbcrt
    
    integer :: ivol
    !f2py intent(inout) ivol
    integer :: imin
    !f2py intent(inout) imin
    call icbcrt(ivol, imin)
end subroutine f90wrap_icbcrt

subroutine f90wrap_icnvrt(way, num, string_bn, length, ierr)
    implicit none
    external icnvrt
    
    integer :: way
    !f2py intent(inout) way
    integer :: num
    !f2py intent(inout) num
    real :: string_bn
    !f2py intent(inout) string_bn
    integer :: length
    !f2py intent(inout) length
    integer :: ierr
    !f2py intent(inout) ierr
    call icnvrt(way, num, string_bn, length, ierr)
end subroutine f90wrap_icnvrt

subroutine f90wrap_icrtlczn(izone)
    implicit none
    external icrtlczn
    
    integer :: izone
    !f2py intent(inout) izone
    call icrtlczn(izone)
end subroutine f90wrap_icrtlczn

subroutine f90wrap_indextec
    implicit none
    external indextec
    
    call indextec()
end subroutine f90wrap_indextec

subroutine f90wrap_infcrt_a(nvx, nvy, nvz, ia, ja, isymm, cinfvs_a, cinfrt_va, &
    cinfrt_da, d, mprop, nzn, diffu, disx, disy, disz, pornew, sanew, uvsnew, &
    hhead, relperm, idbg, ilog, upstream, fully_saturated, variably_saturated, &
    njamxc, nmax, tortuosity_corr, half_cells, sonew, oil_saturation, n0, n1, &
    n2, n3)
    implicit none
    external infcrt_a
    
    integer :: nvx
    !f2py intent(inout) nvx
    integer :: nvy
    !f2py intent(inout) nvy
    integer :: nvz
    !f2py intent(inout) nvz
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    integer, dimension(n2) :: isymm
    !f2py intent(inout) isymm
    real :: cinfvs_a
    !f2py intent(inout) cinfvs_a
    real :: cinfrt_va
    !f2py intent(inout) cinfrt_va
    real :: cinfrt_da
    !f2py intent(inout) cinfrt_da
    real :: d
    !f2py intent(inout) d
    integer, dimension(n3) :: mprop
    !f2py intent(inout) mprop
    integer :: nzn
    !f2py intent(inout) nzn
    real :: diffu
    !f2py intent(inout) diffu
    real :: disx
    !f2py intent(inout) disx
    real :: disy
    !f2py intent(inout) disy
    real :: disz
    !f2py intent(inout) disz
    real :: pornew
    !f2py intent(inout) pornew
    real :: sanew
    !f2py intent(inout) sanew
    real :: uvsnew
    !f2py intent(inout) uvsnew
    real :: hhead
    !f2py intent(inout) hhead
    real :: relperm
    !f2py intent(inout) relperm
    integer :: idbg
    !f2py intent(inout) idbg
    integer :: ilog
    !f2py intent(inout) ilog
    logical :: upstream
    !f2py intent(inout) upstream
    logical :: fully_saturated
    !f2py intent(inout) fully_saturated
    logical :: variably_saturated
    !f2py intent(inout) variably_saturated
    integer :: njamxc
    !f2py intent(inout) njamxc
    integer :: nmax
    !f2py intent(inout) nmax
    real :: tortuosity_corr
    !f2py intent(inout) tortuosity_corr
    logical :: half_cells
    !f2py intent(inout) half_cells
    real :: sonew
    !f2py intent(inout) sonew
    logical :: oil_saturation
    !f2py intent(inout) oil_saturation
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(isymm) :: n2 = shape(isymm,0)
    integer :: n3
    !f2py intent(hide), depend(mprop) :: n3 = shape(mprop,0)
    call infcrt_a(nvx, nvy, nvz, ia, ja, isymm, cinfvs_a, cinfrt_va, cinfrt_da, d, &
        mprop, nzn, diffu, disx, disy, disz, pornew, sanew, uvsnew, hhead, relperm, &
        idbg, ilog, upstream, fully_saturated, variably_saturated, njamxc, nmax, &
        tortuosity_corr, half_cells, sonew, oil_saturation)
end subroutine f90wrap_infcrt_a

subroutine f90wrap_infcrt_g(nx, ny, nz, ia, ja, isymm, cinfrt_dg, d, diffu, &
    pornew, sgnew, idbg, ilog, njamxc, nmax, tortuosity_corr, half_cells, &
    deltaij, tauij, gas_tortuosity, gporij, gsatij, tau_man, sonew, &
    oil_saturation, n0, n1, n2)
    implicit none
    external infcrt_g
    
    integer :: nx
    !f2py intent(inout) nx
    integer :: ny
    !f2py intent(inout) ny
    integer :: nz
    !f2py intent(inout) nz
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    integer, dimension(n2) :: isymm
    !f2py intent(inout) isymm
    real :: cinfrt_dg
    !f2py intent(inout) cinfrt_dg
    real :: d
    !f2py intent(inout) d
    real :: diffu
    !f2py intent(inout) diffu
    real :: pornew
    !f2py intent(inout) pornew
    real :: sgnew
    !f2py intent(inout) sgnew
    integer :: idbg
    !f2py intent(inout) idbg
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: njamxc
    !f2py intent(inout) njamxc
    integer :: nmax
    !f2py intent(inout) nmax
    real :: tortuosity_corr
    !f2py intent(inout) tortuosity_corr
    logical :: half_cells
    !f2py intent(inout) half_cells
    real :: deltaij
    !f2py intent(inout) deltaij
    real :: tauij
    !f2py intent(inout) tauij
    real :: gas_tortuosity
    !f2py intent(inout) gas_tortuosity
    real :: gporij
    !f2py intent(inout) gporij
    real :: gsatij
    !f2py intent(inout) gsatij
    real :: tau_man
    !f2py intent(inout) tau_man
    real :: sonew
    !f2py intent(inout) sonew
    logical :: oil_saturation
    !f2py intent(inout) oil_saturation
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(isymm) :: n2 = shape(isymm,0)
    call infcrt_g(nx, ny, nz, ia, ja, isymm, cinfrt_dg, d, diffu, pornew, sgnew, &
        idbg, ilog, njamxc, nmax, tortuosity_corr, half_cells, deltaij, tauij, &
        gas_tortuosity, gporij, gsatij, tau_man, sonew, oil_saturation)
end subroutine f90wrap_infcrt_g

subroutine f90wrap_infcvs
    implicit none
    external infcvs
    
    call infcvs()
end subroutine f90wrap_infcvs

subroutine f90wrap_infcvs_cp
    implicit none
    external infcvs_cp
    
    call infcvs_cp()
end subroutine f90wrap_infcvs_cp

subroutine f90wrap_initbcrt
    implicit none
    external initbcrt
    
    call initbcrt()
end subroutine f90wrap_initbcrt

subroutine f90wrap_initbcvs
    implicit none
    external initbcvs
    
    call initbcvs()
end subroutine f90wrap_initbcvs

subroutine f90wrap_initcpgs
    implicit none
    external initcpgs
    
    call initcpgs()
end subroutine f90wrap_initcpgs

subroutine f90wrap_initcplc
    implicit none
    external initcplc
    
    call initcplc()
end subroutine f90wrap_initcplc

subroutine f90wrap_initcprt
    implicit none
    external initcprt
    
    call initcprt()
end subroutine f90wrap_initcprt

subroutine f90wrap_initcpvs
    implicit none
    external initcpvs
    
    call initcpvs()
end subroutine f90wrap_initcpvs

subroutine f90wrap_initcsys
    implicit none
    external initcsys
    
    call initcsys()
end subroutine f90wrap_initcsys

subroutine f90wrap_initgeom(im, idbg)
    implicit none
    external initgeom
    
    integer :: im
    !f2py intent(inout) im
    integer :: idbg
    !f2py intent(inout) idbg
    call initgeom(im, idbg)
end subroutine f90wrap_initgeom

subroutine f90wrap_initicrt
    implicit none
    external initicrt
    
    call initicrt()
end subroutine f90wrap_initicrt

subroutine f90wrap_initicvs
    implicit none
    external initicvs
    
    call initicvs()
end subroutine f90wrap_initicvs

subroutine f90wrap_initopgs
    implicit none
    external initopgs
    
    call initopgs()
end subroutine f90wrap_initopgs

subroutine f90wrap_initplant
    implicit none
    external initplant
    
    call initplant()
end subroutine f90wrap_initplant

subroutine f90wrap_initpppm
    implicit none
    external initpppm
    
    call initpppm()
end subroutine f90wrap_initpppm

subroutine f90wrap_initpprt
    implicit none
    external initpprt
    
    call initpprt()
end subroutine f90wrap_initpprt

subroutine f90wrap_initppvs
    implicit none
    external initppvs
    
    call initppvs()
end subroutine f90wrap_initppvs

subroutine f90wrap_initprob
    implicit none
    external initprob
    
    call initprob()
end subroutine f90wrap_initprob

subroutine f90wrap_initsatw
    implicit none
    external initsatw
    
    call initsatw()
end subroutine f90wrap_initsatw

subroutine f90wrap_inittemp
    implicit none
    external inittemp
    
    call inittemp()
end subroutine f90wrap_inittemp

subroutine f90wrap_inittsgs
    implicit none
    external inittsgs
    
    call inittsgs()
end subroutine f90wrap_inittsgs

subroutine f90wrap_initweed
    implicit none
    external initweed
    
    call initweed()
end subroutine f90wrap_initweed

subroutine f90wrap_intpolt
    implicit none
    external intpolt
    
    call intpolt()
end subroutine f90wrap_intpolt

subroutine f90wrap_ionstr(c, cx, strion, chargec, chargex, nc, nx, namec, &
    component_type)
    implicit none
    external ionstr
    
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: strion
    !f2py intent(inout) strion
    real :: chargec
    !f2py intent(inout) chargec
    real :: chargex
    !f2py intent(inout) chargex
    integer :: nc
    !f2py intent(inout) nc
    integer :: nx
    !f2py intent(inout) nx
    integer :: namec
    !f2py intent(inout) namec
    real :: component_type
    !f2py intent(inout) component_type
    call ionstr(c, cx, strion, chargec, chargex, nc, nx, namec, component_type)
end subroutine f90wrap_ionstr

subroutine f90wrap_jacbrt
    implicit none
    external jacbrt
    
    call jacbrt()
end subroutine f90wrap_jacbrt

subroutine f90wrap_jacbvs
    implicit none
    external jacbvs
    
    call jacbvs()
end subroutine f90wrap_jacbvs

subroutine f90wrap_jacfs
    implicit none
    external jacfs
    
    call jacfs()
end subroutine f90wrap_jacfs

subroutine f90wrap_jaclc(cnew, cx, gammac, gammax, sw, sa, por)
    implicit none
    external jaclc
    
    real :: cnew
    !f2py intent(inout) cnew
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: sw
    !f2py intent(inout) sw
    real :: sa
    !f2py intent(inout) sa
    real :: por
    !f2py intent(inout) por
    call jaclc(cnew, cx, gammac, gammax, sw, sa, por)
end subroutine f90wrap_jaclc

subroutine f90wrap_compte
    implicit none
    external compte
    
    call compte()
end subroutine f90wrap_compte

subroutine f90wrap_compte4
    implicit none
    external compte4
    
    call compte4()
end subroutine f90wrap_compte4

subroutine f90wrap_compte5
    implicit none
    external compte5
    
    call compte5()
end subroutine f90wrap_compte5

subroutine f90wrap_compte6
    implicit none
    external compte6
    
    call compte6()
end subroutine f90wrap_compte6

subroutine f90wrap_jacrt
    implicit none
    external jacrt
    
    call jacrt()
end subroutine f90wrap_jacrt

subroutine f90wrap_jacsurf(cnew, gammac, sw, por)
    implicit none
    external jacsurf
    
    real :: cnew
    !f2py intent(inout) cnew
    real :: gammac
    !f2py intent(inout) gammac
    real :: sw
    !f2py intent(inout) sw
    real :: por
    !f2py intent(inout) por
    call jacsurf(cnew, gammac, sw, por)
end subroutine f90wrap_jacsurf

subroutine f90wrap_jacvs
    implicit none
    external jacvs
    
    call jacvs()
end subroutine f90wrap_jacvs

subroutine f90wrap_lennard_jones(sigma, epsil, visc_comp_g, diff_bin_g)
    implicit none
    external lennard_jones
    
    real :: sigma
    !f2py intent(inout) sigma
    real :: epsil
    !f2py intent(inout) epsil
    real :: visc_comp_g
    !f2py intent(inout) visc_comp_g
    real :: diff_bin_g
    !f2py intent(inout) diff_bin_g
    call lennard_jones(sigma, epsil, visc_comp_g, diff_bin_g)
end subroutine f90wrap_lennard_jones

subroutine f90wrap_madd(na, nb, nc, m, n, a, b, c, n0, n1, n2, n3, n4, n5)
    implicit none
    external madd
    
    integer :: na
    !f2py intent(inout) na
    integer :: nb
    !f2py intent(inout) nb
    integer :: nc
    !f2py intent(inout) nc
    integer :: m
    !f2py intent(inout) m
    integer :: n
    !f2py intent(inout) n
    double precision, dimension(n0,n1) :: a
    !f2py intent(inout) a
    double precision, dimension(n2,n3) :: b
    !f2py intent(inout) b
    double precision, dimension(n4,n5) :: c
    !f2py intent(inout) c
    integer :: n0
    !f2py intent(hide), depend(a) :: n0 = shape(a,0)
    integer :: n1
    !f2py intent(hide), depend(a) :: n1 = shape(a,1)
    integer :: n2
    !f2py intent(hide), depend(b) :: n2 = shape(b,0)
    integer :: n3
    !f2py intent(hide), depend(b) :: n3 = shape(b,1)
    integer :: n4
    !f2py intent(hide), depend(c) :: n4 = shape(c,0)
    integer :: n5
    !f2py intent(hide), depend(c) :: n5 = shape(c,1)
    call madd(na, nb, nc, m, n, a, b, c)
end subroutine f90wrap_madd

subroutine f90wrap_mbalrt
    implicit none
    external mbalrt
    
    call mbalrt()
end subroutine f90wrap_mbalrt

subroutine f90wrap_mbalvs
    implicit none
    external mbalvs
    
    call mbalvs()
end subroutine f90wrap_mbalvs

subroutine f90wrap_mem_etr
    implicit none
    external mem_etr
    
    call mem_etr()
end subroutine f90wrap_mem_etr

subroutine f90wrap_mem_mat
    implicit none
    external mem_mat
    
    call mem_mat()
end subroutine f90wrap_mem_mat

subroutine f90wrap_mem_naq
    implicit none
    external mem_naq
    
    call mem_naq()
end subroutine f90wrap_mem_naq

subroutine f90wrap_mem_nc
    implicit none
    external mem_nc
    
    call mem_nc()
end subroutine f90wrap_mem_nc

subroutine f90wrap_mem_ncsb
    implicit none
    external mem_ncsb
    
    call mem_ncsb()
end subroutine f90wrap_mem_ncsb

subroutine f90wrap_mem_ng
    implicit none
    external mem_ng
    
    call mem_ng()
end subroutine f90wrap_mem_ng

subroutine f90wrap_mem_njart
    implicit none
    external mem_njart
    
    call mem_njart()
end subroutine f90wrap_mem_njart

subroutine f90wrap_mem_njavs
    implicit none
    external mem_njavs
    
    call mem_njavs()
end subroutine f90wrap_mem_njavs

subroutine f90wrap_mem_nm
    implicit none
    external mem_nm
    
    call mem_nm()
end subroutine f90wrap_mem_nm

subroutine f90wrap_mem_nmx
    implicit none
    external mem_nmx
    
    call mem_nmx()
end subroutine f90wrap_mem_nmx

subroutine f90wrap_mem_nr
    implicit none
    external mem_nr
    
    call mem_nr()
end subroutine f90wrap_mem_nr

subroutine f90wrap_mem_nsb
    implicit none
    external mem_nsb
    
    call mem_nsb()
end subroutine f90wrap_mem_nsb

subroutine f90wrap_mem_ntmp
    implicit none
    external mem_ntmp
    
    call mem_ntmp()
end subroutine f90wrap_mem_ntmp

subroutine f90wrap_mem_nx
    implicit none
    external mem_nx
    
    call mem_nx()
end subroutine f90wrap_mem_nx

subroutine f90wrap_mem_rt
    implicit none
    external mem_rt
    
    call mem_rt()
end subroutine f90wrap_mem_rt

subroutine f90wrap_mem_vs
    implicit none
    external mem_vs
    
    call mem_vs()
end subroutine f90wrap_mem_vs

subroutine f90wrap_minmaxwd(cx, totc)
    implicit none
    external minmaxwd
    
    real :: cx
    !f2py intent(inout) cx
    real :: totc
    !f2py intent(inout) totc
    call minmaxwd(cx, totc)
end subroutine f90wrap_minmaxwd

subroutine f90wrap_mmul(na, nb, nc, l, m, n, a, b, c, n0, n1, n2, n3, n4, n5)
    implicit none
    external mmul
    
    integer :: na
    !f2py intent(inout) na
    integer :: nb
    !f2py intent(inout) nb
    integer :: nc
    !f2py intent(inout) nc
    integer :: l
    !f2py intent(inout) l
    integer :: m
    !f2py intent(inout) m
    integer :: n
    !f2py intent(inout) n
    double precision, dimension(n0,n1) :: a
    !f2py intent(inout) a
    double precision, dimension(n2,n3) :: b
    !f2py intent(inout) b
    double precision, dimension(n4,n5) :: c
    !f2py intent(inout) c
    integer :: n0
    !f2py intent(hide), depend(a) :: n0 = shape(a,0)
    integer :: n1
    !f2py intent(hide), depend(a) :: n1 = shape(a,1)
    integer :: n2
    !f2py intent(hide), depend(b) :: n2 = shape(b,0)
    integer :: n3
    !f2py intent(hide), depend(b) :: n3 = shape(b,1)
    integer :: n4
    !f2py intent(hide), depend(c) :: n4 = shape(c,0)
    integer :: n5
    !f2py intent(hide), depend(c) :: n5 = shape(c,1)
    call mmul(na, nb, nc, l, m, n, a, b, c)
end subroutine f90wrap_mmul

subroutine f90wrap_modrate(ratem, cmnewm, delt, im)
    implicit none
    external modrate
    
    real :: ratem
    !f2py intent(inout) ratem
    real :: cmnewm
    !f2py intent(inout) cmnewm
    real :: delt
    !f2py intent(inout) delt
    integer :: im
    !f2py intent(inout) im
    call modrate(ratem, cmnewm, delt, im)
end subroutine f90wrap_modrate

subroutine f90wrap_molconc(phim)
    implicit none
    external molconc
    
    real :: phim
    !f2py intent(inout) phim
    call molconc(phim)
end subroutine f90wrap_molconc

subroutine f90wrap_ms_dfluxdg(c_i, c_j, dc_i, dmolfrac_i, zgi, zgj, dens, gpij, &
    tempkel, tauijx, gporx, delta_ijx, small, factor, ipvt, equimolar, ludecomp, &
    fmatx, ms_gflux, ms_dgflux)
    implicit none
    external ms_dfluxdg
    
    real :: c_i
    !f2py intent(inout) c_i
    real :: c_j
    !f2py intent(inout) c_j
    real :: dc_i
    !f2py intent(inout) dc_i
    real :: dmolfrac_i
    !f2py intent(inout) dmolfrac_i
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: dens
    !f2py intent(inout) dens
    real :: gpij
    !f2py intent(inout) gpij
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: tauijx
    !f2py intent(inout) tauijx
    real :: gporx
    !f2py intent(inout) gporx
    real :: delta_ijx
    !f2py intent(inout) delta_ijx
    real :: small
    !f2py intent(inout) small
    real :: factor
    !f2py intent(inout) factor
    integer :: ipvt
    !f2py intent(inout) ipvt
    logical :: equimolar
    !f2py intent(inout) equimolar
    integer :: ludecomp
    !f2py intent(inout) ludecomp
    real :: fmatx
    !f2py intent(inout) fmatx
    integer :: ms_gflux
    !f2py intent(inout) ms_gflux
    integer :: ms_dgflux
    !f2py intent(inout) ms_dgflux
    call ms_dfluxdg(c_i, c_j, dc_i, dmolfrac_i, zgi, zgj, dens, gpij, tempkel, &
        tauijx, gporx, delta_ijx, small, factor, ipvt, equimolar, ludecomp, fmatx, &
        ms_gflux, ms_dgflux)
end subroutine f90wrap_ms_dfluxdg

subroutine f90wrap_ms_fluxdg(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, &
    tempkel, tauijx, gporx, delta_ijx, small, ludecomp, fmat, ipvt, equimolar, &
    ms_gflux, ms_neflux)
    implicit none
    external ms_fluxdg
    
    real :: c_i
    !f2py intent(inout) c_i
    real :: c_j
    !f2py intent(inout) c_j
    real :: c_ij
    !f2py intent(inout) c_ij
    integer :: molfrac
    !f2py intent(inout) molfrac
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: dens
    !f2py intent(inout) dens
    real :: gpij
    !f2py intent(inout) gpij
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: tauijx
    !f2py intent(inout) tauijx
    real :: gporx
    !f2py intent(inout) gporx
    real :: delta_ijx
    !f2py intent(inout) delta_ijx
    real :: small
    !f2py intent(inout) small
    integer :: ludecomp
    !f2py intent(inout) ludecomp
    real :: fmat
    !f2py intent(inout) fmat
    integer :: ipvt
    !f2py intent(inout) ipvt
    logical :: equimolar
    !f2py intent(inout) equimolar
    integer :: ms_gflux
    !f2py intent(inout) ms_gflux
    integer :: ms_neflux
    !f2py intent(inout) ms_neflux
    call ms_fluxdg(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, tauijx, &
        gporx, delta_ijx, small, ludecomp, fmat, ipvt, equimolar, ms_gflux, &
        ms_neflux)
end subroutine f90wrap_ms_fluxdg

subroutine f90wrap_ms_fluxdg_s(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, &
    tempkel, tauijx, gporx, delta_ijx, small, ludecomp, ipvt, equimolar, fmat, &
    ms_neflux_s)
    implicit none
    external ms_fluxdg_s
    
    real :: c_i
    !f2py intent(inout) c_i
    real :: c_j
    !f2py intent(inout) c_j
    real :: c_ij
    !f2py intent(inout) c_ij
    integer :: molfrac
    !f2py intent(inout) molfrac
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: dens
    !f2py intent(inout) dens
    real :: gpij
    !f2py intent(inout) gpij
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: tauijx
    !f2py intent(inout) tauijx
    real :: gporx
    !f2py intent(inout) gporx
    real :: delta_ijx
    !f2py intent(inout) delta_ijx
    real :: small
    !f2py intent(inout) small
    integer :: ludecomp
    !f2py intent(inout) ludecomp
    integer :: ipvt
    !f2py intent(inout) ipvt
    logical :: equimolar
    !f2py intent(inout) equimolar
    real :: fmat
    !f2py intent(inout) fmat
    integer :: ms_neflux_s
    !f2py intent(inout) ms_neflux_s
    call ms_fluxdg_s(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, tauijx, &
        gporx, delta_ijx, small, ludecomp, ipvt, equimolar, fmat, ms_neflux_s)
end subroutine f90wrap_ms_fluxdg_s

subroutine f90wrap_msub(na, nb, nc, m, n, a, b, c, n0, n1, n2, n3, n4, n5)
    implicit none
    external msub
    
    integer :: na
    !f2py intent(inout) na
    integer :: nb
    !f2py intent(inout) nb
    integer :: nc
    !f2py intent(inout) nc
    integer :: m
    !f2py intent(inout) m
    integer :: n
    !f2py intent(inout) n
    double precision, dimension(n0,n1) :: a
    !f2py intent(inout) a
    double precision, dimension(n2,n3) :: b
    !f2py intent(inout) b
    double precision, dimension(n4,n5) :: c
    !f2py intent(inout) c
    integer :: n0
    !f2py intent(hide), depend(a) :: n0 = shape(a,0)
    integer :: n1
    !f2py intent(hide), depend(a) :: n1 = shape(a,1)
    integer :: n2
    !f2py intent(hide), depend(b) :: n2 = shape(b,0)
    integer :: n3
    !f2py intent(hide), depend(b) :: n3 = shape(b,1)
    integer :: n4
    !f2py intent(hide), depend(c) :: n4 = shape(c,0)
    integer :: n5
    !f2py intent(hide), depend(c) :: n5 = shape(c,1)
    call msub(na, nb, nc, m, n, a, b, c)
end subroutine f90wrap_msub

subroutine f90wrap_msysrt
    implicit none
    external msysrt
    
    call msysrt()
end subroutine f90wrap_msysrt

subroutine f90wrap_msysvs
    implicit none
    external msysvs
    
    call msysvs()
end subroutine f90wrap_msysvs

subroutine f90wrap_nexttime
    implicit none
    external nexttime
    
    call nexttime()
end subroutine f90wrap_nexttime

subroutine f90wrap_opndbfls(redox_master, search_database)
    implicit none
    external opndbfls
    
    real :: redox_master
    !f2py intent(inout) redox_master
    logical :: search_database
    !f2py intent(inout) search_database
    call opndbfls(redox_master, search_database)
end subroutine f90wrap_opndbfls

subroutine f90wrap_opngfls
    implicit none
    external opngfls
    
    call opngfls()
end subroutine f90wrap_opngfls

subroutine f90wrap_opnmbfls
    implicit none
    external opnmbfls
    
    call opnmbfls()
end subroutine f90wrap_opnmbfls

subroutine f90wrap_opnpgfls
    implicit none
    external opnpgfls
    
    call opnpgfls()
end subroutine f90wrap_opnpgfls

subroutine f90wrap_opnplfls(ilb)
    implicit none
    external opnplfls
    
    integer :: ilb
    !f2py intent(inout) ilb
    call opnplfls(ilb)
end subroutine f90wrap_opnplfls

subroutine f90wrap_opntemp
    implicit none
    external opntemp
    
    call opntemp()
end subroutine f90wrap_opntemp

subroutine f90wrap_outputlc(c, cx, gammac, gammax, g, igen, ilog, &
    section_header)
    implicit none
    external outputlc
    
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: g
    !f2py intent(inout) g
    integer :: igen
    !f2py intent(inout) igen
    integer :: ilog
    !f2py intent(inout) ilog
    real :: section_header
    !f2py intent(inout) section_header
    call outputlc(c, cx, gammac, gammax, g, igen, ilog, section_header)
end subroutine f90wrap_outputlc

subroutine f90wrap_outputrt
    implicit none
    external outputrt
    
    call outputrt()
end subroutine f90wrap_outputrt

subroutine f90wrap_outputvs
    implicit none
    external outputvs
    
    call outputvs()
end subroutine f90wrap_outputvs

subroutine f90wrap_phcorr(cnew, cold, tempkel, ilog)
    implicit none
    external phcorr
    
    real :: cnew
    !f2py intent(inout) cnew
    real :: cold
    !f2py intent(inout) cold
    real :: tempkel
    !f2py intent(inout) tempkel
    integer :: ilog
    !f2py intent(inout) ilog
    call phcorr(cnew, cold, tempkel, ilog)
end subroutine f90wrap_phcorr

subroutine f90wrap_phpe(c, gammac, ph, pe, eh, tempkel)
    implicit none
    external phpe
    
    real :: c
    !f2py intent(inout) c
    real :: gammac
    !f2py intent(inout) gammac
    real :: ph
    !f2py intent(inout) ph
    real :: pe
    !f2py intent(inout) pe
    real :: eh
    !f2py intent(inout) eh
    real :: tempkel
    !f2py intent(inout) tempkel
    call phpe(c, gammac, ph, pe, eh, tempkel)
end subroutine f90wrap_phpe

subroutine f90wrap_raoult(c, gammac, ratem, phim, phimold, aream, im)
    implicit none
    external raoult
    
    real :: c
    !f2py intent(inout) c
    real :: gammac
    !f2py intent(inout) gammac
    real :: ratem
    !f2py intent(inout) ratem
    real :: phim
    !f2py intent(inout) phim
    real :: phimold
    !f2py intent(inout) phimold
    real :: aream
    !f2py intent(inout) aream
    integer :: im
    !f2py intent(inout) im
    call raoult(c, gammac, ratem, phim, phimold, aream, im)
end subroutine f90wrap_raoult

subroutine f90wrap_rategas(g, tkel, hhead, zg)
    implicit none
    external rategas
    
    real :: g
    !f2py intent(inout) g
    real :: tkel
    !f2py intent(inout) tkel
    real :: hhead
    !f2py intent(inout) hhead
    real :: zg
    !f2py intent(inout) zg
    call rategas(g, tkel, hhead, zg)
end subroutine f90wrap_rategas

subroutine f90wrap_rateh2o
    implicit none
    external rateh2o
    
    call rateh2o()
end subroutine f90wrap_rateh2o

subroutine f90wrap_rateint(rate, totc, c, gammac, phim, iaq)
    implicit none
    external rateint
    
    real :: rate
    !f2py intent(inout) rate
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: gammac
    !f2py intent(inout) gammac
    real :: phim
    !f2py intent(inout) phim
    integer :: iaq
    !f2py intent(inout) iaq
    call rateint(rate, totc, c, gammac, phim, iaq)
end subroutine f90wrap_rateint

subroutine f90wrap_rateint_new(rate, totc, c, cx, gammac, gammax, phim, iaq, sw, &
    por, rootdens, wrf)
    implicit none
    external rateint_new
    
    real :: rate
    !f2py intent(inout) rate
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: phim
    !f2py intent(inout) phim
    integer :: iaq
    !f2py intent(inout) iaq
    real :: sw
    !f2py intent(inout) sw
    real :: por
    !f2py intent(inout) por
    real :: rootdens
    !f2py intent(inout) rootdens
    real :: wrf
    !f2py intent(inout) wrf
    call rateint_new(rate, totc, c, cx, gammac, gammax, phim, iaq, sw, por, &
        rootdens, wrf)
end subroutine f90wrap_rateint_new

subroutine f90wrap_ratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, &
    aream, im)
    implicit none
    external ratemin
    
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: ratem
    !f2py intent(inout) ratem
    real :: phim
    !f2py intent(inout) phim
    real :: phimold
    !f2py intent(inout) phimold
    real :: aream
    !f2py intent(inout) aream
    integer :: im
    !f2py intent(inout) im
    call ratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, im)
end subroutine f90wrap_ratemin

subroutine f90wrap_ratemin_new(totc, c, cx, gammac, gammax, ratem, phim, &
    phimold, aream, im, sw, por, rootdens, rootdens2)
    implicit none
    external ratemin_new
    
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: ratem
    !f2py intent(inout) ratem
    real :: phim
    !f2py intent(inout) phim
    real :: phimold
    !f2py intent(inout) phimold
    real :: aream
    !f2py intent(inout) aream
    integer :: im
    !f2py intent(inout) im
    real :: sw
    !f2py intent(inout) sw
    real :: por
    !f2py intent(inout) por
    real :: rootdens
    !f2py intent(inout) rootdens
    real :: rootdens2
    !f2py intent(inout) rootdens2
    call ratemin_new(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, im, &
        sw, por, rootdens, rootdens2)
end subroutine f90wrap_ratemin_new

subroutine f90wrap_rateredx(c, cx, gammac, gammax, rate, totc, ir)
    implicit none
    external rateredx
    
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: rate
    !f2py intent(inout) rate
    real :: totc
    !f2py intent(inout) totc
    integer :: ir
    !f2py intent(inout) ir
    call rateredx(c, cx, gammac, gammax, rate, totc, ir)
end subroutine f90wrap_rateredx

subroutine f90wrap_reactran
    implicit none
    external reactran
    
    call reactran()
end subroutine f90wrap_reactran

subroutine f90wrap_read_tau
    implicit none
    external read_tau
    
    call read_tau()
end subroutine f90wrap_read_tau

subroutine f90wrap_readbcvs
    implicit none
    external readbcvs
    
    call readbcvs()
end subroutine f90wrap_readbcvs

subroutine f90wrap_readbloc(nin, nout, section_header, found)
    implicit none
    external readbloc
    
    integer :: nin
    !f2py intent(inout) nin
    integer :: nout
    !f2py intent(inout) nout
    real :: section_header
    !f2py intent(inout) section_header
    logical :: found
    !f2py intent(inout) found
    call readbloc(nin, nout, section_header, found)
end subroutine f90wrap_readbloc

subroutine f90wrap_readcomp(icdbs, ilog, idbg)
    implicit none
    external readcomp
    
    integer :: icdbs
    !f2py intent(inout) icdbs
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readcomp(icdbs, ilog, idbg)
end subroutine f90wrap_readcomp

subroutine f90wrap_readgses(igdbs, ipsp, ilog, idbg)
    implicit none
    external readgses
    
    integer :: igdbs
    !f2py intent(inout) igdbs
    integer :: ipsp
    !f2py intent(inout) ipsp
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readgses(igdbs, ipsp, ilog, idbg)
end subroutine f90wrap_readgses

subroutine f90wrap_readint(irdbs, ilog, idbg)
    implicit none
    external readint
    
    integer :: irdbs
    !f2py intent(inout) irdbs
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readint(irdbs, ilog, idbg)
end subroutine f90wrap_readint

subroutine f90wrap_readint_new(irdbs, ilog, idbg)
    implicit none
    external readint_new
    
    integer :: irdbs
    !f2py intent(inout) irdbs
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readint_new(irdbs, ilog, idbg)
end subroutine f90wrap_readint_new

subroutine f90wrap_readmin(imdbs, ilog, idbg, icnv)
    implicit none
    external readmin
    
    integer :: imdbs
    !f2py intent(inout) imdbs
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    integer :: icnv
    !f2py intent(inout) icnv
    call readmin(imdbs, ilog, idbg, icnv)
end subroutine f90wrap_readmin

subroutine f90wrap_readmin_new(imdbs, ilog, idbg, icnv)
    implicit none
    external readmin_new
    
    integer :: imdbs
    !f2py intent(inout) imdbs
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    integer :: icnv
    !f2py intent(inout) icnv
    call readmin_new(imdbs, ilog, idbg, icnv)
end subroutine f90wrap_readmin_new

subroutine f90wrap_readminx(imdbs, ipsp, ilog, idbg)
    implicit none
    external readminx
    
    integer :: imdbs
    !f2py intent(inout) imdbs
    integer :: ipsp
    !f2py intent(inout) ipsp
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readminx(imdbs, ipsp, ilog, idbg)
end subroutine f90wrap_readminx

subroutine f90wrap_readminx_new(imdbs, ipsp, ilog, idbg)
    implicit none
    external readminx_new
    
    integer :: imdbs
    !f2py intent(inout) imdbs
    integer :: ipsp
    !f2py intent(inout) ipsp
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readminx_new(imdbs, ipsp, ilog, idbg)
end subroutine f90wrap_readminx_new

subroutine f90wrap_readredx(irdbs, ilog, idbg)
    implicit none
    external readredx
    
    integer :: irdbs
    !f2py intent(inout) irdbs
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readredx(irdbs, ilog, idbg)
end subroutine f90wrap_readredx

subroutine f90wrap_readredx_new(irdbs, ilog, idbg)
    implicit none
    external readredx_new
    
    integer :: irdbs
    !f2py intent(inout) irdbs
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readredx_new(irdbs, ilog, idbg)
end subroutine f90wrap_readredx_new

subroutine f90wrap_readsorb(isdbs, ipsp, ilog, idbg)
    implicit none
    external readsorb
    
    integer :: isdbs
    !f2py intent(inout) isdbs
    integer :: ipsp
    !f2py intent(inout) ipsp
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readsorb(isdbs, ipsp, ilog, idbg)
end subroutine f90wrap_readsorb

subroutine f90wrap_readsspc(ixdbs, ipsp, ilog, idbg)
    implicit none
    external readsspc
    
    integer :: ixdbs
    !f2py intent(inout) ixdbs
    integer :: ipsp
    !f2py intent(inout) ipsp
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: idbg
    !f2py intent(inout) idbg
    call readsspc(ixdbs, ipsp, ilog, idbg)
end subroutine f90wrap_readsspc

subroutine f90wrap_readtemp
    implicit none
    external readtemp
    
    call readtemp()
end subroutine f90wrap_readtemp

subroutine f90wrap_readtime(nin, nout, ilog, itsrc, found)
    implicit none
    external readtime
    
    integer :: nin
    !f2py intent(inout) nin
    integer :: nout
    !f2py intent(inout) nout
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: itsrc
    !f2py intent(inout) itsrc
    logical :: found
    !f2py intent(inout) found
    call readtime(nin, nout, ilog, itsrc, found)
end subroutine f90wrap_readtime

subroutine f90wrap_readzone(nin, nout, ilog, zone_name, found)
    implicit none
    external readzone
    
    integer :: nin
    !f2py intent(inout) nin
    integer :: nout
    !f2py intent(inout) nout
    integer :: ilog
    !f2py intent(inout) ilog
    real :: zone_name
    !f2py intent(inout) zone_name
    logical :: found
    !f2py intent(inout) found
    call readzone(nin, nout, ilog, zone_name, found)
end subroutine f90wrap_readzone

subroutine f90wrap_restart_r
    implicit none
    external restart_r
    
    call restart_r()
end subroutine f90wrap_restart_r

subroutine f90wrap_restart_w
    implicit none
    external restart_w
    
    call restart_w()
end subroutine f90wrap_restart_w

subroutine f90wrap_rhsrt(naq, ng, nm, nr, nsb, astor, cstor, gstor, totaq, &
    totsb, totor, totdp, totcflux, totgflux, totrateg, redox_equil, &
    noncompetitive_sorption, component_type, b)
    implicit none
    external rhsrt
    
    integer :: naq
    !f2py intent(inout) naq
    integer :: ng
    !f2py intent(inout) ng
    integer :: nm
    !f2py intent(inout) nm
    integer :: nr
    !f2py intent(inout) nr
    integer :: nsb
    !f2py intent(inout) nsb
    real :: astor
    !f2py intent(inout) astor
    real :: cstor
    !f2py intent(inout) cstor
    real :: gstor
    !f2py intent(inout) gstor
    real :: totaq
    !f2py intent(inout) totaq
    real :: totsb
    !f2py intent(inout) totsb
    real :: totor
    !f2py intent(inout) totor
    real :: totdp
    !f2py intent(inout) totdp
    real :: totcflux
    !f2py intent(inout) totcflux
    real :: totgflux
    !f2py intent(inout) totgflux
    real :: totrateg
    !f2py intent(inout) totrateg
    logical :: redox_equil
    !f2py intent(inout) redox_equil
    logical :: noncompetitive_sorption
    !f2py intent(inout) noncompetitive_sorption
    real :: component_type
    !f2py intent(inout) component_type
    real :: b
    !f2py intent(inout) b
    call rhsrt(naq, ng, nm, nr, nsb, astor, cstor, gstor, totaq, totsb, totor, &
        totdp, totcflux, totgflux, totrateg, redox_equil, noncompetitive_sorption, &
        component_type, b)
end subroutine f90wrap_rhsrt

subroutine f90wrap_rhsvs(vsstor, totvsflux, b)
    implicit none
    external rhsvs
    
    real :: vsstor
    !f2py intent(inout) vsstor
    real :: totvsflux
    !f2py intent(inout) totvsflux
    real :: b
    !f2py intent(inout) b
    call rhsvs(vsstor, totvsflux, b)
end subroutine f90wrap_rhsvs

subroutine f90wrap_rsort(rlist, n)
    implicit none
    external rsort
    
    real :: rlist
    !f2py intent(inout) rlist
    integer :: n
    !f2py intent(inout) n
    call rsort(rlist, n)
end subroutine f90wrap_rsort

subroutine f90wrap_rstatgs(idev)
    implicit none
    external rstatgs
    
    integer :: idev
    !f2py intent(inout) idev
    call rstatgs(idev)
end subroutine f90wrap_rstatgs

subroutine f90wrap_rstatlc(idev)
    implicit none
    external rstatlc
    
    integer :: idev
    !f2py intent(inout) idev
    call rstatlc(idev)
end subroutine f90wrap_rstatlc

subroutine f90wrap_rtrvpprm(swc, sac, porc, section_header)
    implicit none
    external rtrvpprm
    
    real :: swc
    !f2py intent(inout) swc
    real :: sac
    !f2py intent(inout) sac
    real :: porc
    !f2py intent(inout) porc
    real :: section_header
    !f2py intent(inout) section_header
    call rtrvpprm(swc, sac, porc, section_header)
end subroutine f90wrap_rtrvpprm

subroutine f90wrap_secspec(c, c2, eqc2, gammac1, gammac2, xnuc2, ia, ja, n, i2)
    implicit none
    external secspec
    
    real :: c
    !f2py intent(inout) c
    real :: c2
    !f2py intent(inout) c2
    real :: eqc2
    !f2py intent(inout) eqc2
    real :: gammac1
    !f2py intent(inout) gammac1
    real :: gammac2
    !f2py intent(inout) gammac2
    real :: xnuc2
    !f2py intent(inout) xnuc2
    integer :: ia
    !f2py intent(inout) ia
    integer :: ja
    !f2py intent(inout) ja
    integer :: n
    !f2py intent(inout) n
    integer :: i2
    !f2py intent(inout) i2
    call secspec(c, c2, eqc2, gammac1, gammac2, xnuc2, ia, ja, n, i2)
end subroutine f90wrap_secspec

subroutine f90wrap_seepface
    implicit none
    external seepface
    
    call seepface()
end subroutine f90wrap_seepface

subroutine f90wrap_setsize(redox_equil_s)
    implicit none
    external setsize
    
    logical :: redox_equil_s
    !f2py intent(inout) redox_equil_s
    call setsize(redox_equil_s)
end subroutine f90wrap_setsize

subroutine f90wrap_simq(z, y, n, nxdim)
    implicit none
    external simq
    
    real :: z
    !f2py intent(inout) z
    real :: y
    !f2py intent(inout) y
    integer :: n
    !f2py intent(inout) n
    integer :: nxdim
    !f2py intent(inout) nxdim
    call simq(z, y, n, nxdim)
end subroutine f90wrap_simq

subroutine f90wrap_soilparm(uvsnew, sanew, relperm, relpermg, sonew, mpropvs, &
    nn)
    implicit none
    external soilparm
    
    real :: uvsnew
    !f2py intent(inout) uvsnew
    real :: sanew
    !f2py intent(inout) sanew
    real :: relperm
    !f2py intent(inout) relperm
    real :: relpermg
    !f2py intent(inout) relpermg
    real :: sonew
    !f2py intent(inout) sonew
    integer :: mpropvs
    !f2py intent(inout) mpropvs
    integer :: nn
    !f2py intent(inout) nn
    call soilparm(uvsnew, sanew, relperm, relpermg, sonew, mpropvs, nn)
end subroutine f90wrap_soilparm

subroutine f90wrap_sorbconc(tota, totc, distcoff, sw, por, ilog)
    implicit none
    external sorbconc
    
    real :: tota
    !f2py intent(inout) tota
    real :: totc
    !f2py intent(inout) totc
    real :: distcoff
    !f2py intent(inout) distcoff
    real :: sw
    !f2py intent(inout) sw
    real :: por
    !f2py intent(inout) por
    integer :: ilog
    !f2py intent(inout) ilog
    call sorbconc(tota, totc, distcoff, sw, por, ilog)
end subroutine f90wrap_sorbconc

subroutine f90wrap_sorbspc(csb, cec, eqsb, gammac, c, xnusb, iasb, jasb, nsb, &
    isb, sorption_type, sorption_group, component_type, nc, chargesb, namesb, &
    totco, nelec)
    implicit none
    external sorbspc
    
    real :: csb
    !f2py intent(inout) csb
    real :: cec
    !f2py intent(inout) cec
    real :: eqsb
    !f2py intent(inout) eqsb
    real :: gammac
    !f2py intent(inout) gammac
    real :: c
    !f2py intent(inout) c
    real :: xnusb
    !f2py intent(inout) xnusb
    integer :: iasb
    !f2py intent(inout) iasb
    integer :: jasb
    !f2py intent(inout) jasb
    integer :: nsb
    !f2py intent(inout) nsb
    integer :: isb
    !f2py intent(inout) isb
    real :: sorption_type
    !f2py intent(inout) sorption_type
    real :: sorption_group
    !f2py intent(inout) sorption_group
    real :: component_type
    !f2py intent(inout) component_type
    integer :: nc
    !f2py intent(inout) nc
    real :: chargesb
    !f2py intent(inout) chargesb
    integer :: namesb
    !f2py intent(inout) namesb
    real :: totco
    !f2py intent(inout) totco
    integer :: nelec
    !f2py intent(inout) nelec
    call sorbspc(csb, cec, eqsb, gammac, c, xnusb, iasb, jasb, nsb, isb, &
        sorption_type, sorption_group, component_type, nc, chargesb, namesb, totco, &
        nelec)
end subroutine f90wrap_sorbspc

subroutine f90wrap_sortcomp(idbg, ilog)
    implicit none
    external sortcomp
    
    integer :: idbg
    !f2py intent(inout) idbg
    integer :: ilog
    !f2py intent(inout) ilog
    call sortcomp(idbg, ilog)
end subroutine f90wrap_sortcomp

subroutine f90wrap_sptldisc
    implicit none
    external sptldisc
    
    call sptldisc()
end subroutine f90wrap_sptldisc

subroutine f90wrap_stedflow
    implicit none
    external stedflow
    
    call stedflow()
end subroutine f90wrap_stedflow

subroutine f90wrap_surfcomp(cnew, gammac, sw, por, ilog)
    implicit none
    external surfcomp
    
    real :: cnew
    !f2py intent(inout) cnew
    real :: gammac
    !f2py intent(inout) gammac
    real :: sw
    !f2py intent(inout) sw
    real :: por
    !f2py intent(inout) por
    integer :: ilog
    !f2py intent(inout) ilog
    call surfcomp(cnew, gammac, sw, por, ilog)
end subroutine f90wrap_surfcomp

subroutine f90wrap_tcorr(tempkel)
    implicit none
    external tcorr
    
    real :: tempkel
    !f2py intent(inout) tempkel
    call tcorr(tempkel)
end subroutine f90wrap_tcorr

subroutine f90wrap_timeloop
    implicit none
    external timeloop
    
    call timeloop()
end subroutine f90wrap_timeloop

subroutine f90wrap_totcona(tota, totc, distcoff, sw, por)
    implicit none
    external totcona
    
    real :: tota
    !f2py intent(inout) tota
    real :: totc
    !f2py intent(inout) totc
    real :: distcoff
    !f2py intent(inout) distcoff
    real :: sw
    !f2py intent(inout) sw
    real :: por
    !f2py intent(inout) por
    call totcona(tota, totc, distcoff, sw, por)
end subroutine f90wrap_totcona

subroutine f90wrap_totconc(c, cx, totc)
    implicit none
    external totconc
    
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: totc
    !f2py intent(inout) totc
    call totconc(c, cx, totc)
end subroutine f90wrap_totconc

subroutine f90wrap_totconcg(g, totg)
    implicit none
    external totconcg
    
    real :: g
    !f2py intent(inout) g
    real :: totg
    !f2py intent(inout) totg
    call totconcg(g, totg)
end subroutine f90wrap_totconcg

subroutine f90wrap_totconcsb(tota, totc, distcoff, expfr, langmuir, pol, sw, &
    por)
    implicit none
    external totconcsb
    
    real :: tota
    !f2py intent(inout) tota
    real :: totc
    !f2py intent(inout) totc
    real :: distcoff
    !f2py intent(inout) distcoff
    real :: expfr
    !f2py intent(inout) expfr
    integer :: langmuir
    !f2py intent(inout) langmuir
    real :: pol
    !f2py intent(inout) pol
    real :: sw
    !f2py intent(inout) sw
    real :: por
    !f2py intent(inout) por
    call totconcsb(tota, totc, distcoff, expfr, langmuir, pol, sw, por)
end subroutine f90wrap_totconcsb

subroutine f90wrap_totint(totintaq, idbg)
    implicit none
    external totint
    
    real :: totintaq
    !f2py intent(inout) totintaq
    integer :: idbg
    !f2py intent(inout) idbg
    call totint(totintaq, idbg)
end subroutine f90wrap_totint

subroutine f90wrap_totint_w(totintaq_w, idbg)
    implicit none
    external totint_w
    
    real :: totintaq_w
    !f2py intent(inout) totintaq_w
    integer :: idbg
    !f2py intent(inout) idbg
    call totint_w(totintaq_w, idbg)
end subroutine f90wrap_totint_w

subroutine f90wrap_totmin(ratem, totm)
    implicit none
    external totmin
    
    real :: ratem
    !f2py intent(inout) ratem
    real :: totm
    !f2py intent(inout) totm
    call totmin(ratem, totm)
end subroutine f90wrap_totmin

subroutine f90wrap_totmin_w(ratem, totm_w)
    implicit none
    external totmin_w
    
    real :: ratem
    !f2py intent(inout) ratem
    real :: totm_w
    !f2py intent(inout) totm_w
    call totmin_w(ratem, totm_w)
end subroutine f90wrap_totmin_w

subroutine f90wrap_totredx(totoxrd, idbg)
    implicit none
    external totredx
    
    real :: totoxrd
    !f2py intent(inout) totoxrd
    integer :: idbg
    !f2py intent(inout) idbg
    call totredx(totoxrd, idbg)
end subroutine f90wrap_totredx

subroutine f90wrap_totredx_w(totoxrd_w, idbg)
    implicit none
    external totredx_w
    
    real :: totoxrd_w
    !f2py intent(inout) totoxrd_w
    integer :: idbg
    !f2py intent(inout) idbg
    call totredx_w(totoxrd_w, idbg)
end subroutine f90wrap_totredx_w

subroutine f90wrap_totsorb(csb, chargesb, rhobulk, totcsb, xnusb, iasb, jasb, &
    nc, nsb, namec, sorption_group, component_type)
    implicit none
    external totsorb
    
    real :: csb
    !f2py intent(inout) csb
    real :: chargesb
    !f2py intent(inout) chargesb
    real :: rhobulk
    !f2py intent(inout) rhobulk
    real :: totcsb
    !f2py intent(inout) totcsb
    real :: xnusb
    !f2py intent(inout) xnusb
    integer :: iasb
    !f2py intent(inout) iasb
    integer :: jasb
    !f2py intent(inout) jasb
    integer :: nc
    !f2py intent(inout) nc
    integer :: nsb
    !f2py intent(inout) nsb
    integer :: namec
    !f2py intent(inout) namec
    real :: sorption_group
    !f2py intent(inout) sorption_group
    real :: component_type
    !f2py intent(inout) component_type
    call totsorb(csb, chargesb, rhobulk, totcsb, xnusb, iasb, jasb, nc, nsb, namec, &
        sorption_group, component_type)
end subroutine f90wrap_totsorb

subroutine f90wrap_tprfrtlc(totc, c, cx, gammac, gammax, cm, g, cec_l, distcoff, &
    aream, phim, phimold, strion, tempkel, hhead, zg, time, deltat, sw, porvol, &
    iunit1, iunit2, iunit3, iunit4, iunit11, iunit5, iunit6, iunit7, iunit8, &
    iunit9, iunit10, prefix, l_prfx, tec_header, ivolume, ntstp, zone_name, &
    l_zone_name, update_porosity)
    implicit none
    external tprfrtlc
    
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: cm
    !f2py intent(inout) cm
    real :: g
    !f2py intent(inout) g
    real :: cec_l
    !f2py intent(inout) cec_l
    real :: distcoff
    !f2py intent(inout) distcoff
    real :: aream
    !f2py intent(inout) aream
    real :: phim
    !f2py intent(inout) phim
    real :: phimold
    !f2py intent(inout) phimold
    real :: strion
    !f2py intent(inout) strion
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: hhead
    !f2py intent(inout) hhead
    real :: zg
    !f2py intent(inout) zg
    real :: time
    !f2py intent(inout) time
    real :: deltat
    !f2py intent(inout) deltat
    real :: sw
    !f2py intent(inout) sw
    real :: porvol
    !f2py intent(inout) porvol
    integer :: iunit1
    !f2py intent(inout) iunit1
    integer :: iunit2
    !f2py intent(inout) iunit2
    integer :: iunit3
    !f2py intent(inout) iunit3
    integer :: iunit4
    !f2py intent(inout) iunit4
    integer :: iunit11
    !f2py intent(inout) iunit11
    integer :: iunit5
    !f2py intent(inout) iunit5
    integer :: iunit6
    !f2py intent(inout) iunit6
    integer :: iunit7
    !f2py intent(inout) iunit7
    integer :: iunit8
    !f2py intent(inout) iunit8
    integer :: iunit9
    !f2py intent(inout) iunit9
    integer :: iunit10
    !f2py intent(inout) iunit10
    real :: prefix
    !f2py intent(inout) prefix
    integer :: l_prfx
    !f2py intent(inout) l_prfx
    logical :: tec_header
    !f2py intent(inout) tec_header
    integer :: ivolume
    !f2py intent(inout) ivolume
    integer :: ntstp
    !f2py intent(inout) ntstp
    real :: zone_name
    !f2py intent(inout) zone_name
    integer :: l_zone_name
    !f2py intent(inout) l_zone_name
    logical :: update_porosity
    !f2py intent(inout) update_porosity
    call tprfrtlc(totc, c, cx, gammac, gammax, cm, g, cec_l, distcoff, aream, phim, &
        phimold, strion, tempkel, hhead, zg, time, deltat, sw, porvol, iunit1, &
        iunit2, iunit3, iunit4, iunit11, iunit5, iunit6, iunit7, iunit8, iunit9, &
        iunit10, prefix, l_prfx, tec_header, ivolume, ntstp, zone_name, l_zone_name, &
        update_porosity)
end subroutine f90wrap_tprfrtlc

subroutine f90wrap_tprfrtlcg0(totc, c, cx, gammac, gammax, cm, cec_l, distcoff, &
    aream, phim, phimold, strion, tempkel, hhead, zg, time, deltat, sw, porvol, &
    iunit1, iunit2, iunit3, iunit11, iunit5, iunit6, iunit7, iunit8, iunit9, &
    iunit10, prefix, l_prfx, tec_header, ivolume, ntstp, zone_name, l_zone_name, &
    update_porosity)
    implicit none
    external tprfrtlcg0
    
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: cm
    !f2py intent(inout) cm
    real :: cec_l
    !f2py intent(inout) cec_l
    real :: distcoff
    !f2py intent(inout) distcoff
    real :: aream
    !f2py intent(inout) aream
    real :: phim
    !f2py intent(inout) phim
    real :: phimold
    !f2py intent(inout) phimold
    real :: strion
    !f2py intent(inout) strion
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: hhead
    !f2py intent(inout) hhead
    real :: zg
    !f2py intent(inout) zg
    real :: time
    !f2py intent(inout) time
    real :: deltat
    !f2py intent(inout) deltat
    real :: sw
    !f2py intent(inout) sw
    real :: porvol
    !f2py intent(inout) porvol
    integer :: iunit1
    !f2py intent(inout) iunit1
    integer :: iunit2
    !f2py intent(inout) iunit2
    integer :: iunit3
    !f2py intent(inout) iunit3
    integer :: iunit11
    !f2py intent(inout) iunit11
    integer :: iunit5
    !f2py intent(inout) iunit5
    integer :: iunit6
    !f2py intent(inout) iunit6
    integer :: iunit7
    !f2py intent(inout) iunit7
    integer :: iunit8
    !f2py intent(inout) iunit8
    integer :: iunit9
    !f2py intent(inout) iunit9
    integer :: iunit10
    !f2py intent(inout) iunit10
    real :: prefix
    !f2py intent(inout) prefix
    integer :: l_prfx
    !f2py intent(inout) l_prfx
    logical :: tec_header
    !f2py intent(inout) tec_header
    integer :: ivolume
    !f2py intent(inout) ivolume
    integer :: ntstp
    !f2py intent(inout) ntstp
    real :: zone_name
    !f2py intent(inout) zone_name
    integer :: l_zone_name
    !f2py intent(inout) l_zone_name
    logical :: update_porosity
    !f2py intent(inout) update_porosity
    call tprfrtlcg0(totc, c, cx, gammac, gammax, cm, cec_l, distcoff, aream, phim, &
        phimold, strion, tempkel, hhead, zg, time, deltat, sw, porvol, iunit1, &
        iunit2, iunit3, iunit11, iunit5, iunit6, iunit7, iunit8, iunit9, iunit10, &
        prefix, l_prfx, tec_header, ivolume, ntstp, zone_name, l_zone_name, &
        update_porosity)
end subroutine f90wrap_tprfrtlcg0

subroutine f90wrap_tprfrtlcm0(totc, c, cx, gammac, gammax, g, cec_l, distcoff, &
    strion, tempkel, hhead, zg, time, deltat, sw, porvol, iunit1, iunit2, &
    iunit3, iunit4, iunit11, iunit5, iunit6, iunit10, prefix, l_prfx, &
    tec_header, ivolume, ntstp, zone_name, l_zone_name, update_porosity)
    implicit none
    external tprfrtlcm0
    
    real :: totc
    !f2py intent(inout) totc
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: g
    !f2py intent(inout) g
    real :: cec_l
    !f2py intent(inout) cec_l
    real :: distcoff
    !f2py intent(inout) distcoff
    real :: strion
    !f2py intent(inout) strion
    real :: tempkel
    !f2py intent(inout) tempkel
    real :: hhead
    !f2py intent(inout) hhead
    real :: zg
    !f2py intent(inout) zg
    real :: time
    !f2py intent(inout) time
    real :: deltat
    !f2py intent(inout) deltat
    real :: sw
    !f2py intent(inout) sw
    real :: porvol
    !f2py intent(inout) porvol
    integer :: iunit1
    !f2py intent(inout) iunit1
    integer :: iunit2
    !f2py intent(inout) iunit2
    integer :: iunit3
    !f2py intent(inout) iunit3
    integer :: iunit4
    !f2py intent(inout) iunit4
    integer :: iunit11
    !f2py intent(inout) iunit11
    integer :: iunit5
    !f2py intent(inout) iunit5
    integer :: iunit6
    !f2py intent(inout) iunit6
    integer :: iunit10
    !f2py intent(inout) iunit10
    real :: prefix
    !f2py intent(inout) prefix
    integer :: l_prfx
    !f2py intent(inout) l_prfx
    logical :: tec_header
    !f2py intent(inout) tec_header
    integer :: ivolume
    !f2py intent(inout) ivolume
    integer :: ntstp
    !f2py intent(inout) ntstp
    real :: zone_name
    !f2py intent(inout) zone_name
    integer :: l_zone_name
    !f2py intent(inout) l_zone_name
    logical :: update_porosity
    !f2py intent(inout) update_porosity
    call tprfrtlcm0(totc, c, cx, gammac, gammax, g, cec_l, distcoff, strion, &
        tempkel, hhead, zg, time, deltat, sw, porvol, iunit1, iunit2, iunit3, &
        iunit4, iunit11, iunit5, iunit6, iunit10, prefix, l_prfx, tec_header, &
        ivolume, ntstp, zone_name, l_zone_name, update_porosity)
end subroutine f90wrap_tprfrtlcm0

subroutine f90wrap_tprfvs(ivol)
    implicit none
    external tprfvs
    
    integer :: ivol
    !f2py intent(inout) ivol
    call tprfvs(ivol)
end subroutine f90wrap_tprfvs

subroutine f90wrap_tranbcrt
    implicit none
    external tranbcrt
    
    call tranbcrt()
end subroutine f90wrap_tranbcrt

subroutine f90wrap_tranflow
    implicit none
    external tranflow
    
    call tranflow()
end subroutine f90wrap_tranflow

subroutine f90wrap_tranunit(igb)
    implicit none
    external tranunit
    
    integer :: igb
    !f2py intent(inout) igb
    call tranunit(igb)
end subroutine f90wrap_tranunit

subroutine f90wrap_tsteplc(cnew, cold, ulc)
    implicit none
    external tsteplc
    
    real :: cnew
    !f2py intent(inout) cnew
    real :: cold
    !f2py intent(inout) cold
    real :: ulc
    !f2py intent(inout) ulc
    call tsteplc(cnew, cold, ulc)
end subroutine f90wrap_tsteplc

subroutine f90wrap_tsteprt
    implicit none
    external tsteprt
    
    call tsteprt()
end subroutine f90wrap_tsteprt

subroutine f90wrap_tstepvs
    implicit none
    external tstepvs
    
    call tstepvs()
end subroutine f90wrap_tstepvs

subroutine f90wrap_update_tau(im, tivol)
    implicit none
    external update_tau
    
    integer :: im
    !f2py intent(inout) im
    real :: tivol
    !f2py intent(inout) tivol
    call update_tau(im, tivol)
end subroutine f90wrap_update_tau

subroutine f90wrap_updatelc(c, ulc, ilog, not_converged, zone_name)
    implicit none
    external updatelc
    
    real :: c
    !f2py intent(inout) c
    real :: ulc
    !f2py intent(inout) ulc
    integer :: ilog
    !f2py intent(inout) ilog
    logical :: not_converged
    !f2py intent(inout) not_converged
    real :: zone_name
    !f2py intent(inout) zone_name
    call updatelc(c, ulc, ilog, not_converged, zone_name)
end subroutine f90wrap_updatelc

subroutine f90wrap_updatert
    implicit none
    external updatert
    
    call updatert()
end subroutine f90wrap_updatert

subroutine f90wrap_updatevs
    implicit none
    external updatevs
    
    call updatevs()
end subroutine f90wrap_updatevs

subroutine f90wrap_updtbcvs
    implicit none
    external updtbcvs
    
    call updtbcvs()
end subroutine f90wrap_updtbcvs

subroutine f90wrap_updtetp
    implicit none
    external updtetp
    
    call updtetp()
end subroutine f90wrap_updtetp

subroutine f90wrap_updtrootdensity
    implicit none
    external updtrootdensity
    
    call updtrootdensity()
end subroutine f90wrap_updtrootdensity

subroutine f90wrap_updtsurf(c, ulc, ilog, not_converged)
    implicit none
    external updtsurf
    
    real :: c
    !f2py intent(inout) c
    real :: ulc
    !f2py intent(inout) ulc
    integer :: ilog
    !f2py intent(inout) ilog
    logical :: not_converged
    !f2py intent(inout) not_converged
    call updtsurf(c, ulc, ilog, not_converged)
end subroutine f90wrap_updtsurf

subroutine f90wrap_updtsvap(c, cx, gammac, gammax, strion)
    implicit none
    external updtsvap
    
    real :: c
    !f2py intent(inout) c
    real :: cx
    !f2py intent(inout) cx
    real :: gammac
    !f2py intent(inout) gammac
    real :: gammax
    !f2py intent(inout) gammax
    real :: strion
    !f2py intent(inout) strion
    call updtsvap(c, cx, gammac, gammax, strion)
end subroutine f90wrap_updtsvap

subroutine f90wrap_updtsvgp(c, gammac, g, totcg, tempkel)
    implicit none
    external updtsvgp
    
    real :: c
    !f2py intent(inout) c
    real :: gammac
    !f2py intent(inout) gammac
    real :: g
    !f2py intent(inout) g
    real :: totcg
    !f2py intent(inout) totcg
    real :: tempkel
    !f2py intent(inout) tempkel
    call updtsvgp(c, gammac, g, totcg, tempkel)
end subroutine f90wrap_updtsvgp

subroutine f90wrap_updtsvmp(cmnewm, cmoldm, phim, aream, ratem, delt)
    implicit none
    external updtsvmp
    
    real :: cmnewm
    !f2py intent(inout) cmnewm
    real :: cmoldm
    !f2py intent(inout) cmoldm
    real :: phim
    !f2py intent(inout) phim
    real :: aream
    !f2py intent(inout) aream
    real :: ratem
    !f2py intent(inout) ratem
    real :: delt
    !f2py intent(inout) delt
    call updtsvmp(cmnewm, cmoldm, phim, aream, ratem, delt)
end subroutine f90wrap_updtsvmp

subroutine f90wrap_velocity(nvx, nvy, nvz, iavs, javs, cinfvs_a, dimcv, xg, yg, &
    zg, uvsnew, hhead, relperm, idbg, ilog, ivel, upstream, fully_saturated, &
    njavs, nn, half_cells, n0, n1)
    implicit none
    external velocity
    
    integer :: nvx
    !f2py intent(inout) nvx
    integer :: nvy
    !f2py intent(inout) nvy
    integer :: nvz
    !f2py intent(inout) nvz
    integer, dimension(n0) :: iavs
    !f2py intent(inout) iavs
    integer, dimension(n1) :: javs
    !f2py intent(inout) javs
    real :: cinfvs_a
    !f2py intent(inout) cinfvs_a
    real :: dimcv
    !f2py intent(inout) dimcv
    real :: xg
    !f2py intent(inout) xg
    real :: yg
    !f2py intent(inout) yg
    real :: zg
    !f2py intent(inout) zg
    real :: uvsnew
    !f2py intent(inout) uvsnew
    real :: hhead
    !f2py intent(inout) hhead
    real :: relperm
    !f2py intent(inout) relperm
    integer :: idbg
    !f2py intent(inout) idbg
    integer :: ilog
    !f2py intent(inout) ilog
    integer :: ivel
    !f2py intent(inout) ivel
    logical :: upstream
    !f2py intent(inout) upstream
    logical :: fully_saturated
    !f2py intent(inout) fully_saturated
    integer :: njavs
    !f2py intent(inout) njavs
    integer :: nn
    !f2py intent(inout) nn
    logical :: half_cells
    !f2py intent(inout) half_cells
    integer :: n0
    !f2py intent(hide), depend(iavs) :: n0 = shape(iavs,0)
    integer :: n1
    !f2py intent(hide), depend(javs) :: n1 = shape(javs,0)
    call velocity(nvx, nvy, nvz, iavs, javs, cinfvs_a, dimcv, xg, yg, zg, uvsnew, &
        hhead, relperm, idbg, ilog, ivel, upstream, fully_saturated, njavs, nn, &
        half_cells)
end subroutine f90wrap_velocity

subroutine f90wrap_velocityg(l_sufx, suffix)
    implicit none
    external velocityg
    
    integer :: l_sufx
    !f2py intent(inout) l_sufx
    real :: suffix
    !f2py intent(inout) suffix
    call velocityg(l_sufx, suffix)
end subroutine f90wrap_velocityg

subroutine f90wrap_vsflow
    implicit none
    external vsflow
    
    call vsflow()
end subroutine f90wrap_vsflow

subroutine f90wrap_weed
    implicit none
    external weed
    
    call weed()
end subroutine f90wrap_weed

subroutine f90wrap_welcome
    implicit none
    external welcome
    
    call welcome()
end subroutine f90wrap_welcome

subroutine f90wrap_wgprop(totg_i, totg_j, totg, g_i, g_j, g, molfrac_i, &
    molfrac_j, molfracg, relpermg_i, relpermg_j, relpg, dens_i, dens_j, densg, &
    visc_i, visc_j, viscg, gpi, gpj, gpij, zgi, zgj, spt_weight, iupsgx, nc, ng, &
    gacc)
    implicit none
    external wgprop
    
    real :: totg_i
    !f2py intent(inout) totg_i
    real :: totg_j
    !f2py intent(inout) totg_j
    real :: totg
    !f2py intent(inout) totg
    real :: g_i
    !f2py intent(inout) g_i
    real :: g_j
    !f2py intent(inout) g_j
    real :: g
    !f2py intent(inout) g
    integer :: molfrac_i
    !f2py intent(inout) molfrac_i
    integer :: molfrac_j
    !f2py intent(inout) molfrac_j
    integer :: molfracg
    !f2py intent(inout) molfracg
    real :: relpermg_i
    !f2py intent(inout) relpermg_i
    real :: relpermg_j
    !f2py intent(inout) relpermg_j
    real :: relpg
    !f2py intent(inout) relpg
    real :: dens_i
    !f2py intent(inout) dens_i
    real :: dens_j
    !f2py intent(inout) dens_j
    real :: densg
    !f2py intent(inout) densg
    real :: visc_i
    !f2py intent(inout) visc_i
    real :: visc_j
    !f2py intent(inout) visc_j
    real :: viscg
    !f2py intent(inout) viscg
    real :: gpi
    !f2py intent(inout) gpi
    real :: gpj
    !f2py intent(inout) gpj
    real :: gpij
    !f2py intent(inout) gpij
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: spt_weight
    !f2py intent(inout) spt_weight
    integer :: iupsgx
    !f2py intent(inout) iupsgx
    integer :: nc
    !f2py intent(inout) nc
    integer :: ng
    !f2py intent(inout) ng
    real :: gacc
    !f2py intent(inout) gacc
    call wgprop(totg_i, totg_j, totg, g_i, g_j, g, molfrac_i, molfrac_j, molfracg, &
        relpermg_i, relpermg_j, relpg, dens_i, dens_j, densg, visc_i, visc_j, viscg, &
        gpi, gpj, gpij, zgi, zgj, spt_weight, iupsgx, nc, ng, gacc)
end subroutine f90wrap_wgprop

subroutine f90wrap_wgpropd(totg_i, totg_j, totg, relpermg_i, relpermg_j, relpg, &
    dens_i, dens_j, densg, visc_i, visc_j, viscg, gpi, gpj, gpij, zgi, zgj, &
    spt_weight, iupsgx, factor, nc, ng, gacc)
    implicit none
    external wgpropd
    
    real :: totg_i
    !f2py intent(inout) totg_i
    real :: totg_j
    !f2py intent(inout) totg_j
    real :: totg
    !f2py intent(inout) totg
    real :: relpermg_i
    !f2py intent(inout) relpermg_i
    real :: relpermg_j
    !f2py intent(inout) relpermg_j
    real :: relpg
    !f2py intent(inout) relpg
    real :: dens_i
    !f2py intent(inout) dens_i
    real :: dens_j
    !f2py intent(inout) dens_j
    real :: densg
    !f2py intent(inout) densg
    real :: visc_i
    !f2py intent(inout) visc_i
    real :: visc_j
    !f2py intent(inout) visc_j
    real :: viscg
    !f2py intent(inout) viscg
    real :: gpi
    !f2py intent(inout) gpi
    real :: gpj
    !f2py intent(inout) gpj
    real :: gpij
    !f2py intent(inout) gpij
    real :: zgi
    !f2py intent(inout) zgi
    real :: zgj
    !f2py intent(inout) zgj
    real :: spt_weight
    !f2py intent(inout) spt_weight
    integer :: iupsgx
    !f2py intent(inout) iupsgx
    real :: factor
    !f2py intent(inout) factor
    integer :: nc
    !f2py intent(inout) nc
    integer :: ng
    !f2py intent(inout) ng
    real :: gacc
    !f2py intent(inout) gacc
    call wgpropd(totg_i, totg_j, totg, relpermg_i, relpermg_j, relpg, dens_i, &
        dens_j, densg, visc_i, visc_j, viscg, gpi, gpj, gpij, zgi, zgj, spt_weight, &
        iupsgx, factor, nc, ng, gacc)
end subroutine f90wrap_wgpropd

subroutine f90wrap_ws209(lfile, nn, nitmax, numit, idetail, ia, ja, iaf, iafd, &
    jaf, lorder, a, af, x, b, res, work, restol, deltol, nja, njaf, over_flow, &
    rnorm, rmupdate, n0, n1, n2, n3, n4, n5)
    implicit none
    external ws209
    
    integer :: lfile
    !f2py intent(inout) lfile
    integer :: nn
    !f2py intent(inout) nn
    integer :: nitmax
    !f2py intent(inout) nitmax
    integer :: numit
    !f2py intent(inout) numit
    integer :: idetail
    !f2py intent(inout) idetail
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    integer, dimension(n2) :: iaf
    !f2py intent(inout) iaf
    integer, dimension(n3) :: iafd
    !f2py intent(inout) iafd
    integer, dimension(n4) :: jaf
    !f2py intent(inout) jaf
    integer, dimension(n5) :: lorder
    !f2py intent(inout) lorder
    real :: a
    !f2py intent(inout) a
    real :: af
    !f2py intent(inout) af
    real :: x
    !f2py intent(inout) x
    real :: b
    !f2py intent(inout) b
    real :: res
    !f2py intent(inout) res
    real :: work
    !f2py intent(inout) work
    real :: restol
    !f2py intent(inout) restol
    real :: deltol
    !f2py intent(inout) deltol
    integer :: nja
    !f2py intent(inout) nja
    integer :: njaf
    !f2py intent(inout) njaf
    logical :: over_flow
    !f2py intent(inout) over_flow
    real :: rnorm
    !f2py intent(inout) rnorm
    real :: rmupdate
    !f2py intent(inout) rmupdate
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(iaf) :: n2 = shape(iaf,0)
    integer :: n3
    !f2py intent(hide), depend(iafd) :: n3 = shape(iafd,0)
    integer :: n4
    !f2py intent(hide), depend(jaf) :: n4 = shape(jaf,0)
    integer :: n5
    !f2py intent(hide), depend(lorder) :: n5 = shape(lorder,0)
    call ws209(lfile, nn, nitmax, numit, idetail, ia, ja, iaf, iafd, jaf, lorder, a, &
        af, x, b, res, work, restol, deltol, nja, njaf, over_flow, rnorm, rmupdate)
end subroutine f90wrap_ws209

subroutine f90wrap_bicgstab(lfile, nn, idetail, nitmax, numit, ia, ja, iaf, &
    iafd, jaf, converged, a, af, x, res, restol, rnorm, rmupdate, deltol, res0, &
    pvec, vbar, avbar, svec, zvec, tvec, temp, lorder, nja, njaf, n0, n1, n2, &
    n3, n4, n5)
    implicit none
    external bicgstab
    
    integer :: lfile
    !f2py intent(inout) lfile
    integer :: nn
    !f2py intent(inout) nn
    integer :: idetail
    !f2py intent(inout) idetail
    integer :: nitmax
    !f2py intent(inout) nitmax
    integer :: numit
    !f2py intent(inout) numit
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    integer, dimension(n2) :: iaf
    !f2py intent(inout) iaf
    integer, dimension(n3) :: iafd
    !f2py intent(inout) iafd
    integer, dimension(n4) :: jaf
    !f2py intent(inout) jaf
    logical :: converged
    !f2py intent(inout) converged
    real :: a
    !f2py intent(inout) a
    real :: af
    !f2py intent(inout) af
    real :: x
    !f2py intent(inout) x
    real :: res
    !f2py intent(inout) res
    real :: restol
    !f2py intent(inout) restol
    real :: rnorm
    !f2py intent(inout) rnorm
    real :: rmupdate
    !f2py intent(inout) rmupdate
    real :: deltol
    !f2py intent(inout) deltol
    real :: res0
    !f2py intent(inout) res0
    real :: pvec
    !f2py intent(inout) pvec
    real :: vbar
    !f2py intent(inout) vbar
    real :: avbar
    !f2py intent(inout) avbar
    real :: svec
    !f2py intent(inout) svec
    real :: zvec
    !f2py intent(inout) zvec
    real :: tvec
    !f2py intent(inout) tvec
    real :: temp
    !f2py intent(inout) temp
    integer, dimension(n5) :: lorder
    !f2py intent(inout) lorder
    integer :: nja
    !f2py intent(inout) nja
    integer :: njaf
    !f2py intent(inout) njaf
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(iaf) :: n2 = shape(iaf,0)
    integer :: n3
    !f2py intent(hide), depend(iafd) :: n3 = shape(iafd,0)
    integer :: n4
    !f2py intent(hide), depend(jaf) :: n4 = shape(jaf,0)
    integer :: n5
    !f2py intent(hide), depend(lorder) :: n5 = shape(lorder,0)
    call bicgstab(lfile, nn, idetail, nitmax, numit, ia, ja, iaf, iafd, jaf, &
        converged, a, af, x, res, restol, rnorm, rmupdate, deltol, res0, pvec, vbar, &
        avbar, svec, zvec, tvec, temp, lorder, nja, njaf)
end subroutine f90wrap_bicgstab

subroutine f90wrap_loweruppersolve(nn, njaf, x, b, af, temp, iaf, iafd, jaf, &
    lorder, n0, n1, n2, n3)
    implicit none
    external loweruppersolve
    
    integer :: nn
    !f2py intent(inout) nn
    integer :: njaf
    !f2py intent(inout) njaf
    real :: x
    !f2py intent(inout) x
    real :: b
    !f2py intent(inout) b
    real :: af
    !f2py intent(inout) af
    real :: temp
    !f2py intent(inout) temp
    integer, dimension(n0) :: iaf
    !f2py intent(inout) iaf
    integer, dimension(n1) :: iafd
    !f2py intent(inout) iafd
    integer, dimension(n2) :: jaf
    !f2py intent(inout) jaf
    integer, dimension(n3) :: lorder
    !f2py intent(inout) lorder
    integer :: n0
    !f2py intent(hide), depend(iaf) :: n0 = shape(iaf,0)
    integer :: n1
    !f2py intent(hide), depend(iafd) :: n1 = shape(iafd,0)
    integer :: n2
    !f2py intent(hide), depend(jaf) :: n2 = shape(jaf,0)
    integer :: n3
    !f2py intent(hide), depend(lorder) :: n3 = shape(lorder,0)
    call loweruppersolve(nn, njaf, x, b, af, temp, iaf, iafd, jaf, lorder)
end subroutine f90wrap_loweruppersolve

subroutine f90wrap_matrixvectormultiply(nn, nja, x, b, a, ia, ja, n0, n1)
    implicit none
    external matrixvectormultiply
    
    integer :: nn
    !f2py intent(inout) nn
    integer :: nja
    !f2py intent(inout) nja
    real :: x
    !f2py intent(inout) x
    real :: b
    !f2py intent(inout) b
    real :: a
    !f2py intent(inout) a
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    call matrixvectormultiply(nn, nja, x, b, a, ia, ja)
end subroutine f90wrap_matrixvectormultiply

subroutine f90wrap_idamax(n, ret_idamax, dx)
    implicit none
    external idamax
    integer idamax
    
    integer :: n
    !f2py intent(inout) n
    integer, intent(out) :: ret_idamax
    real :: dx
    !f2py intent(inout) dx
    ret_idamax = idamax(n, dx)
end subroutine f90wrap_idamax

subroutine f90wrap_incompletefactorization(nn, nja, njaf, b, a, af, row, ia, ja, &
    iaf, iafd, jaf, list, lorder, invord, n0, n1, n2, n3, n4, n5, n6, n7)
    implicit none
    external incompletefactorization
    
    integer :: nn
    !f2py intent(inout) nn
    integer :: nja
    !f2py intent(inout) nja
    integer :: njaf
    !f2py intent(inout) njaf
    real :: b
    !f2py intent(inout) b
    real :: a
    !f2py intent(inout) a
    real :: af
    !f2py intent(inout) af
    real :: row
    !f2py intent(inout) row
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    integer, dimension(n2) :: iaf
    !f2py intent(inout) iaf
    integer, dimension(n3) :: iafd
    !f2py intent(inout) iafd
    integer, dimension(n4) :: jaf
    !f2py intent(inout) jaf
    integer, dimension(n5) :: list
    !f2py intent(inout) list
    integer, dimension(n6) :: lorder
    !f2py intent(inout) lorder
    integer, dimension(n7) :: invord
    !f2py intent(inout) invord
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(iaf) :: n2 = shape(iaf,0)
    integer :: n3
    !f2py intent(hide), depend(iafd) :: n3 = shape(iafd,0)
    integer :: n4
    !f2py intent(hide), depend(jaf) :: n4 = shape(jaf,0)
    integer :: n5
    !f2py intent(hide), depend(list) :: n5 = shape(list,0)
    integer :: n6
    !f2py intent(hide), depend(lorder) :: n6 = shape(lorder,0)
    integer :: n7
    !f2py intent(hide), depend(invord) :: n7 = shape(invord,0)
    call incompletefactorization(nn, nja, njaf, b, a, af, row, ia, ja, iaf, iafd, &
        jaf, list, lorder, invord)
end subroutine f90wrap_incompletefactorization

subroutine f90wrap_symbolicfactorization(lfile, nn, nja, njaf, mnjaf, level, &
    list, ia, ja, row, levptr, iaf, iafd, jaf, lorder, invord, n0, n1, n2, n3, &
    n4, n5, n6, n7, n8, n9)
    implicit none
    external symbolicfactorization
    
    integer :: lfile
    !f2py intent(inout) lfile
    integer :: nn
    !f2py intent(inout) nn
    integer :: nja
    !f2py intent(inout) nja
    integer :: njaf
    !f2py intent(inout) njaf
    integer :: mnjaf
    !f2py intent(inout) mnjaf
    integer :: level
    !f2py intent(inout) level
    integer, dimension(n0) :: list
    !f2py intent(inout) list
    integer, dimension(n1) :: ia
    !f2py intent(inout) ia
    integer, dimension(n2) :: ja
    !f2py intent(inout) ja
    integer, dimension(n3) :: row
    !f2py intent(inout) row
    integer, dimension(n4) :: levptr
    !f2py intent(inout) levptr
    integer, dimension(n5) :: iaf
    !f2py intent(inout) iaf
    integer, dimension(n6) :: iafd
    !f2py intent(inout) iafd
    integer, dimension(n7) :: jaf
    !f2py intent(inout) jaf
    integer, dimension(n8) :: lorder
    !f2py intent(inout) lorder
    integer, dimension(n9) :: invord
    !f2py intent(inout) invord
    integer :: n0
    !f2py intent(hide), depend(list) :: n0 = shape(list,0)
    integer :: n1
    !f2py intent(hide), depend(ia) :: n1 = shape(ia,0)
    integer :: n2
    !f2py intent(hide), depend(ja) :: n2 = shape(ja,0)
    integer :: n3
    !f2py intent(hide), depend(row) :: n3 = shape(row,0)
    integer :: n4
    !f2py intent(hide), depend(levptr) :: n4 = shape(levptr,0)
    integer :: n5
    !f2py intent(hide), depend(iaf) :: n5 = shape(iaf,0)
    integer :: n6
    !f2py intent(hide), depend(iafd) :: n6 = shape(iafd,0)
    integer :: n7
    !f2py intent(hide), depend(jaf) :: n7 = shape(jaf,0)
    integer :: n8
    !f2py intent(hide), depend(lorder) :: n8 = shape(lorder,0)
    integer :: n9
    !f2py intent(hide), depend(invord) :: n9 = shape(invord,0)
    call symbolicfactorization(lfile, nn, nja, njaf, mnjaf, level, list, ia, ja, &
        row, levptr, iaf, iafd, jaf, lorder, invord)
end subroutine f90wrap_symbolicfactorization

subroutine f90wrap_naturalordering(nn, lorder, invord, n0, n1)
    implicit none
    external naturalordering
    
    integer :: nn
    !f2py intent(inout) nn
    integer, dimension(n0) :: lorder
    !f2py intent(inout) lorder
    integer, dimension(n1) :: invord
    !f2py intent(inout) invord
    integer :: n0
    !f2py intent(hide), depend(lorder) :: n0 = shape(lorder,0)
    integer :: n1
    !f2py intent(hide), depend(invord) :: n1 = shape(invord,0)
    call naturalordering(nn, lorder, invord)
end subroutine f90wrap_naturalordering

subroutine f90wrap_rcmordering(nn, nja, ia, ja, lorder, invord, mask, xls, n0, &
    n1, n2, n3, n4, n5)
    implicit none
    external rcmordering
    
    integer :: nn
    !f2py intent(inout) nn
    integer :: nja
    !f2py intent(inout) nja
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    integer, dimension(n2) :: lorder
    !f2py intent(inout) lorder
    integer, dimension(n3) :: invord
    !f2py intent(inout) invord
    logical, dimension(n4) :: mask
    !f2py intent(inout) mask
    integer, dimension(n5) :: xls
    !f2py intent(inout) xls
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(lorder) :: n2 = shape(lorder,0)
    integer :: n3
    !f2py intent(hide), depend(invord) :: n3 = shape(invord,0)
    integer :: n4
    !f2py intent(hide), depend(mask) :: n4 = shape(mask,0)
    integer :: n5
    !f2py intent(hide), depend(xls) :: n5 = shape(xls,0)
    call rcmordering(nn, nja, ia, ja, lorder, invord, mask, xls)
end subroutine f90wrap_rcmordering

subroutine f90wrap_findperipheralnode(nn, nja, rnode, ia, ja, mask, nlvl, xls, &
    ls, n0, n1, n2, n3, n4)
    implicit none
    external findperipheralnode
    
    integer :: nn
    !f2py intent(inout) nn
    integer :: nja
    !f2py intent(inout) nja
    integer :: rnode
    !f2py intent(inout) rnode
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    logical, dimension(n2) :: mask
    !f2py intent(inout) mask
    integer :: nlvl
    !f2py intent(inout) nlvl
    integer, dimension(n3) :: xls
    !f2py intent(inout) xls
    integer, dimension(n4) :: ls
    !f2py intent(inout) ls
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(mask) :: n2 = shape(mask,0)
    integer :: n3
    !f2py intent(hide), depend(xls) :: n3 = shape(xls,0)
    integer :: n4
    !f2py intent(hide), depend(ls) :: n4 = shape(ls,0)
    call findperipheralnode(nn, nja, rnode, ia, ja, mask, nlvl, xls, ls)
end subroutine f90wrap_findperipheralnode

subroutine f90wrap_rootedlevelstructure(nn, nja, rnode, ia, ja, mask, nlvl, xls, &
    ls, n0, n1, n2, n3, n4)
    implicit none
    external rootedlevelstructure
    
    integer :: nn
    !f2py intent(inout) nn
    integer :: nja
    !f2py intent(inout) nja
    integer :: rnode
    !f2py intent(inout) rnode
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    logical, dimension(n2) :: mask
    !f2py intent(inout) mask
    integer :: nlvl
    !f2py intent(inout) nlvl
    integer, dimension(n3) :: xls
    !f2py intent(inout) xls
    integer, dimension(n4) :: ls
    !f2py intent(inout) ls
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(mask) :: n2 = shape(mask,0)
    integer :: n3
    !f2py intent(hide), depend(xls) :: n3 = shape(xls,0)
    integer :: n4
    !f2py intent(hide), depend(ls) :: n4 = shape(ls,0)
    call rootedlevelstructure(nn, nja, rnode, ia, ja, mask, nlvl, xls, ls)
end subroutine f90wrap_rootedlevelstructure

subroutine f90wrap_reversecuthillmckee(nn, nja, rnode, ia, ja, mask, lorder, &
    ccsize, deg, n0, n1, n2, n3, n4)
    implicit none
    external reversecuthillmckee
    
    integer :: nn
    !f2py intent(inout) nn
    integer :: nja
    !f2py intent(inout) nja
    integer :: rnode
    !f2py intent(inout) rnode
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    logical, dimension(n2) :: mask
    !f2py intent(inout) mask
    integer, dimension(n3) :: lorder
    !f2py intent(inout) lorder
    integer :: ccsize
    !f2py intent(inout) ccsize
    integer, dimension(n4) :: deg
    !f2py intent(inout) deg
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(mask) :: n2 = shape(mask,0)
    integer :: n3
    !f2py intent(hide), depend(lorder) :: n3 = shape(lorder,0)
    integer :: n4
    !f2py intent(hide), depend(deg) :: n4 = shape(deg,0)
    call reversecuthillmckee(nn, nja, rnode, ia, ja, mask, lorder, ccsize, deg)
end subroutine f90wrap_reversecuthillmckee

subroutine f90wrap_degree(nn, nja, rnode, ia, ja, mask, deg, ccsize, ls, n0, n1, &
    n2, n3, n4)
    implicit none
    external degree
    
    integer :: nn
    !f2py intent(inout) nn
    integer :: nja
    !f2py intent(inout) nja
    integer :: rnode
    !f2py intent(inout) rnode
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    logical, dimension(n2) :: mask
    !f2py intent(inout) mask
    integer, dimension(n3) :: deg
    !f2py intent(inout) deg
    integer :: ccsize
    !f2py intent(inout) ccsize
    integer, dimension(n4) :: ls
    !f2py intent(inout) ls
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    integer :: n2
    !f2py intent(hide), depend(mask) :: n2 = shape(mask,0)
    integer :: n3
    !f2py intent(hide), depend(deg) :: n3 = shape(deg,0)
    integer :: n4
    !f2py intent(hide), depend(ls) :: n4 = shape(ls,0)
    call degree(nn, nja, rnode, ia, ja, mask, deg, ccsize, ls)
end subroutine f90wrap_degree

subroutine f90wrap_bubblesort(list, n, n0)
    implicit none
    external bubblesort
    
    integer, dimension(n0) :: list
    !f2py intent(inout) list
    integer :: n
    !f2py intent(inout) n
    integer :: n0
    !f2py intent(hide), depend(list) :: n0 = shape(list,0)
    call bubblesort(list, n)
end subroutine f90wrap_bubblesort

subroutine f90wrap_binaryfind(nn, nja, ia, ja, jband, nj, ni, n0, n1)
    implicit none
    external binaryfind
    
    integer :: nn
    !f2py intent(inout) nn
    integer :: nja
    !f2py intent(inout) nja
    integer, dimension(n0) :: ia
    !f2py intent(inout) ia
    integer, dimension(n1) :: ja
    !f2py intent(inout) ja
    integer :: jband
    !f2py intent(inout) jband
    integer :: nj
    !f2py intent(inout) nj
    integer :: ni
    !f2py intent(inout) ni
    integer :: n0
    !f2py intent(hide), depend(ia) :: n0 = shape(ia,0)
    integer :: n1
    !f2py intent(hide), depend(ja) :: n1 = shape(ja,0)
    call binaryfind(nn, nja, ia, ja, jband, nj, ni)
end subroutine f90wrap_binaryfind

subroutine f90wrap_check(number, maximum, lfile)
    implicit none
    external check
    
    integer :: number
    !f2py intent(inout) number
    integer :: maximum
    !f2py intent(inout) maximum
    integer :: lfile
    !f2py intent(inout) lfile
    call check(number, maximum, lfile)
end subroutine f90wrap_check

subroutine f90wrap_xyzcoord
    implicit none
    external xyzcoord
    
    call xyzcoord()
end subroutine f90wrap_xyzcoord

subroutine f90wrap_zero_i4(i4, n1, n2, n3)
    implicit none
    external zero_i4
    
    integer :: i4
    !f2py intent(inout) i4
    integer :: n1
    !f2py intent(inout) n1
    integer :: n2
    !f2py intent(inout) n2
    integer :: n3
    !f2py intent(inout) n3
    call zero_i4(i4, n1, n2, n3)
end subroutine f90wrap_zero_i4

subroutine f90wrap_zero_r8(r8, n1, n2, n3)
    implicit none
    external zero_r8
    
    real :: r8
    !f2py intent(inout) r8
    integer :: n1
    !f2py intent(inout) n1
    integer :: n2
    !f2py intent(inout) n2
    integer :: n3
    !f2py intent(inout) n3
    call zero_r8(r8, n1, n2, n3)
end subroutine f90wrap_zero_r8

