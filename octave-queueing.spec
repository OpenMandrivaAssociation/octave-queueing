%define octpkg queueing

Summary:	Functions for queueing networks and Markov chains analysis with Octave
Name:		octave-%{octpkg}
Version:	1.2.5
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.8.1

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

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

