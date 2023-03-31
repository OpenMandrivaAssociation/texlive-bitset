Name:		texlive-bitset
Version:	53837
Release:	2
Summary:	Handle bit-vector datatype
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bitset
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitset.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitset.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitset.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines and implements the data type bit set, a
vector of bits. The size of the vector may grow dynamically.
Individual bits can be manipulated.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bitset
%{_texmfdistdir}/tex/generic/bitset
%doc %{_texmfdistdir}/doc/latex/bitset

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
