%global octpkg queueing

Summary:	Functions for queueing networks and Markov chains analysis with Octave
Name:		octave-queueing
Version:	1.2.7
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/queueing/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?48959
Patch0:		doc-Makefile.patch

BuildRequires:  octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Functions for queueing networks, discrete- and continuous-time Markov
chains analysis. Compute steady-state performance measures for open,
closed and mixed networks with single or multiple job classes, mean
Value Analysis (MVA), convolution, and various bounding techniques.
Furthermore, several transient and steady-state performance measures
for Markov chains can be computed, such as state occupancy
probabilities, mean time to absorption, time-averaged sojourn times
and so forth.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

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

