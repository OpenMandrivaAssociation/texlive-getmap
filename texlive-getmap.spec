%global tl_name getmap
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.11
Release:	%{tl_revision}.1
Summary:	Download OpenStreetMap maps for use in documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/getmap
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/getmap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/getmap.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(getmap.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple interface to OpenStreetMap, and to Google
Maps "map images". In the simplest case, it is sufficient to specify the
address you need (if you don't, the package will use its own default).
The package loads the map image using an external lua script (invoked
via \write 18: LaTeX must be running with \write 18 enabled). The
("external") lua script may be used from the command line; a bash
version is provided.

