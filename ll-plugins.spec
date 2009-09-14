Summary:	A collection of LV2 plugins
Name:		ll-plugins
Version:	0.2.1
Release:	%mkrel 2
License:	GPLv3+
Group:		Sound
URL:		http://ll-plugins.nongnu.org/index.html
Source0:	http://download.savannah.nongnu.org/releases/ll-plugins/%{name}-%{version}.tar.bz2
Requires:	jackit >= 0.109
BuildRequires:	alsa-lib-devel
BuildRequires:	boost-devel
BuildRequires:	cairomm-devel
BuildRequires:	fftw3-devel
BuildRequires:	gsl-devel
BuildRequires:	gtkmm2.4-devel >= 2.6.0
BuildRequires:	jackit
BuildRequires:	lash-devel
BuildRequires:	libjack-devel >= 0.109
BuildRequires:	liblo-devel
BuildRequires:	lv2-c++-tools
BuildRequires:	lv2-c++-tools-devel
BuildRequires:	pkgconfig
BuildRequires:	libsamplerate-devel
BuildRequires:	sndfile-devel
BuildRequires:	sigc++2.0-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
THE PLUGINS
===========
All plugins are installed in separate LV2 bundles (except the ones that are
closely related, like the math-constant plugins or the mono and stereo versions
of the peak meter). The GUIs, for the plugins that have GUIs, are installed in
bundles of their own to make it easier for packagers to put them in separate
binary packages to avoid Gtk dependencies for the plugins themselves.

The plugins are reasonably simple and could be used as examples or starting 
points for hackers who want to write LV2 plugins based on the frameworks in
the lv2-c++-tools package. There are synths, event processors, simple audio
and control manipulators and GUI-based plugins.

BASIC ARPEGGIATOR
=================
This plugin is just what it says. It takes MIDI event input and writes
MIDI event output in the form of an arpeggio over the held keys in the input.
You can control the speed of the arpeggio and the direction (up or down).

CONTROL2MIDI
============
A plugin that converts a LV2 control port value to MIDI CC events. You can 
set the CC number and the expected range of the input value.

KLAVIATUR
=========
A MIDI keyboard. You can use it to send pitchbend events, CC events and of 
course notes, using mouse or keyboard. Handy when you want to test a synth
patch but don't have a real keyboard nearby. Klaviatur has a Gtk GUI that you
use to control it.

MATH-CONSTANTS
==============
A set of plugins that output constant control parameters for mathematical
constants defined in the C header <math.h>.

MATH-FUNCTIONS
==============
A set of plugins wrapping most of the functions in the C header <math.h>
(sin(), cos(), exp(), modf() etc). All are available as both audio rate
and control rate functions.

PEAK METER
==========
A decaying peak meter that shows the peak level of the input signal.
There is a mono and a stereo version. Both have Gtk GUIs.

RUDOLF 556
==========
A simple drum machine with six separate drum voices - two bass drums, two
snares and two hihats. The different voices are mapped to C, D, E, F, G and A
in all octaves, and every voice has three control parameters (length, 
hardness and volume). This plugin has a Gtk GUI that you can use to control the
parameters.

SINESHAPER
==========
An LV2 version of the Sineshaper synth - two sine oscillators fed through
two sine waveshapers in series, with a bunch of parameters to control them.
This plugin has a Gtk GUI too.

%package	gui
Summary:	GUIs for the ll-plugins package
Group:		Sound

%description	gui
This package contains the GUIs for the ll-plugins.

%package -n	elven
Summary:	The LV2 host Elven
Group:		Sound
Requires:	jackit >= 0.109

%description -n	elven
THE HOST
========
The host that comes with this package is called Elven (Experimental LV2 
Execution ENvironment). It is pretty slow and I don't really recommend it.
If you can use another host, do that.

%prep

%setup -q -n %{name}-%{version}

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--CFLAGS="%{optflags} -Dclear_path=begin_new_path"

%make

%install
rm -rf %{buildroot}

%makeinstall_std \
	build_experimental=yes \
	install-lv2-plugins \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	docdir=%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lv2/arpeggiator.lv2/*
%{_libdir}/lv2/control2midi.lv2/*
%{_libdir}/lv2/klaviatur.lv2/*
%{_libdir}/lv2/math-constants.lv2/*
%{_libdir}/lv2/math-functions.lv2/*
%{_libdir}/lv2/peakmeter.lv2/*
%{_libdir}/lv2/rudolf556.lv2/*
%{_libdir}/lv2/sineshaper.lv2/*

%files gui
%defattr(-, root, root)
%doc COPYING
%{_libdir}/lv2/klaviatur_gtk.lv2/*
%{_libdir}/lv2/peakmeter_gtk.lv2/*
%{_libdir}/lv2/rudolf556_gtk.lv2/*
%{_libdir}/lv2/sineshaper_gtk.lv2/*

%files -n elven
%defattr(-, root, root)
%doc COPYING
%{_bindir}/elven

