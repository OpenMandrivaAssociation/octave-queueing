%global octpkg queueing

Summary:	Functions for queueing networks and Markov chains analysis with Octave
Name:		octave-%{octpkg}
Version:	1.2.7
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?48959
Patch0:		doc-Makefile.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The queueing package provides functions for queueing networks and Markov
chains analysis. This package can be used to compute steady-state
performance measures for open, closed and mixed networks with single or
multiple job classes. Mean Value Analysis (MVA), convolution, and various
bounding techniques are implemented. Furthermore, several transient and
steady-state performance measures for Markov chains can be computed, such
as state occupancy probabilities, mean time to absorption, time-averaged
sojourn times and so forth. Discrete- and continuous-time Markov chains
are supported.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

