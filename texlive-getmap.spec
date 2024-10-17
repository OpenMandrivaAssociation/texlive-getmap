Name:		texlive-getmap
Version:	50589
Release:	2
Summary:	Download OpenStreetMap maps for use in documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/getmap
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getmap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getmap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple interface to OpenStreetMap, and
to Google Maps "map images". In the simplest case, it is
sufficient to specify the address you need (if you don't, the
package will use its own default). The package loads the map
image using an external lua script (invoked via \write 18:
LaTeX must be running with \write 18 enabled). The ("external")
lua script may be used from the command line; a bash version is
provided.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/latex/getmap
%{_texmfdistdir}/texmf-dist/scripts/getmap
%doc %{_texmfdistdir}/texmf-dist/doc/latex/getmap

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
