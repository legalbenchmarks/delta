<p align="center">
  <img src="docs/assets/hero.png" alt="Dutch Legal AI Benchmark, door Legal Benchmarks en Zeno" width="820">
</p>

<p align="center">
  DELTA: Dutch Legal AI Benchmark
</p>

<p align="center">
  <img src="https://img.shields.io/badge/taken-15-F16411" alt="15 taken">
  <img src="https://img.shields.io/badge/criteria-273-F16411" alt="273 criteria">
  <a href="https://github.com/legalbenchmarks/delta/actions/workflows/validate.yml"><img src="https://github.com/legalbenchmarks/delta/actions/workflows/validate.yml/badge.svg" alt="Validatiestatus"></a>
</p>

<p align="center">
  <em>English: <a href="README.md">README.md</a></em> · Geen GitHub-gebruiker? <a href="https://drive.google.com/drive/folders/1zQn89pcsmAJ0-y9hy--TIbbkgXvUyZtN">Google Drive-map</a>
</p>

DELTA is een openbare, door de juridische praktijk geleide benchmark die meet hoe foundation models presteren op realistisch Nederlands juridisch werk. De benchmark vraagt niet alleen of AI het recht juist toepast, maar ook of het werk blijk geeft van **legal taste**: het professionele oordeelsvermogen om vast te stellen wat ertoe doet en een antwoord te leveren waarmee een jurist kan werken.

De eerste openbare release van DELTA richt zich op juridisch onderzoek met open vragen. De opensource-taakset is geselecteerd uit meer dan 200 juridische opdrachten die vragen uit de Nederlandse rechtspraktijk weerspiegelen. De benchmarkresultaten van de eerste openbare release worden binnenkort gepubliceerd.

Meer dan honderd juristen in Nederland hielpen DELTA vorm te geven. Het bijbehorende onderzoeksrapport onderzoekt hoe Nederlandse juristen AI gebruiken, waar AI tekortschiet, welke risico’s zij het ernstigst vinden en wanneer een antwoord professioneel aanvaardbaar blijft, ook als het nog moet worden gecorrigeerd.

DELTA wordt samengesteld en onderhouden door [Legal Benchmarks](https://www.legalbenchmarks.ai/), met [Zeno](https://zeno.law/) als Founding Research Partner.

## Onderzoek

<!-- Omslaggeometrie naar Piet Mondriaan. -->
<table>
<tr>
<td align="center"><a href="https://www.legalbenchmarks.ai/research/delta"><img src="docs/assets/adoption-survey-cover.png" width="400" alt="Dutch legal AI adoption survey report, aug 2026"></a><br><sub>Dutch Legal AI Adoption Survey Report</sub></td>
</tr>
</table>

## De taken

Elke taak presenteert een vraag waarmee een Nederlandse jurist in de praktijk te maken kan krijgen, gesteld in het Nederlands met een Engelse referentievertaling. Nederlandse juristen uit de praktijk hebben de vragen beoordeeld en modeluitvoer gescoord. Hun beoordelingen hebben bijgedragen aan de ontwikkeling en kalibratie van het raamwerk.

Elke taak vermeldt de peildatum voor het juridisch onderzoek in `law_as_of`.

De beoordelingscriteria vallen in drie categorieën:

- **Substance**: is de juridische analyse juist, volledig en professioneel verdedigbaar
- **Citation**: wordt de bepalende rechtsbron juist genoemd
- **Form**: kan een juridische professional het antwoord gebruiken zoals het is aangeleverd

**Legal taste omvat zowel substance als form.** De substance-criteria meten professioneel oordeel, waaronder de vraag of het antwoord de beslissende kwesties identificeert, hoofdzaken van bijzaken onderscheidt en voorbehouden passend doseert. De form-criteria meten de laatste stap: of het antwoord geprioriteerd, proportioneel, gestructureerd en bruikbaar is.

De form-criteria codificeren bewust taakgebonden professionele voorkeuren. Als een criterium voorschrijft dat de conclusie in de openingsalinea staat of dat bijkomend materiaal ondergeschikt blijft, maakt dat deel uit van de gepubliceerde beoordelingsnorm voor die opdracht. Deze eisen zijn expliciet, waarneembaar en betwistbaar; beoordelaars mogen geen voorkeuren toevoegen die niet in het criterium staan.

Voor analyse krijgt elk criterium dat geen citation-criterium is ook beschrijvende `dimensions`: juridische juistheid of juridisch oordeel voor substance, en bruikbaarheid of stijl voor form. Deze tags beschrijven wat het criterium meet; de uitgeschreven criteriumtekst blijft de enige beoordelingsnorm.

| Rechtsgebied | Taken | Criteria |
|---|---:|---:|
| [Aansprakelijkheidsrecht](tasks/tort-law) | 3 | 49 |
| [Goederenrecht](tasks/property-law) | 2 | 48 |
| [Ondernemingsrecht](tasks/corporate-law) | 2 | 36 |
| [Insolventierecht en herstructurering](tasks/insolvency-restructuring) | 2 | 33 |
| [Vastgoedrecht](tasks/real-estate) | 2 | 32 |
| [Contractenrecht](tasks/contract-law) | 1 | 24 |
| [Arbeidsrecht](tasks/employment-law) | 1 | 22 |
| [Mededingingsrecht](tasks/competition-law) | 1 | 18 |
| [Personen- en familierecht](tasks/family-law) | 1 | 11 |

Elke taak is een map onder [`tasks/`](tasks); de volledige set staat ook in één machineleesbaar bestand, [`data/tasks.jsonl`](data/tasks.jsonl).

## Gebruik

Een systeem beoordelen vraagt twee onderdelen:

- een **harness** die elke prompt aan het systeem voorlegt en de antwoorden vastlegt
- een **judge** die de antwoorden beoordeelt aan de hand van de criteria

| Documentatie | |
|---|---|
| [docs/harness.md](docs/harness.md) | Harnessprotocol, vaste prompt en registratieformaat |
| [docs/judge.md](docs/judge.md) | Antwoorden beoordelen: assen, blind beoordelen, metrieken |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Taken toevoegen, criteria betwisten |

## Deelnemende kantoren

<table>
<tr>
<td align="center" width="25%"><a href="https://www.banning.nl/"><img src="docs/assets/firms/banning.svg" height="34" alt="Banning Advocaten"></a></td>
<td align="center" width="25%"><a href="https://www.bvd-advocaten.nl/"><img src="docs/assets/firms/bvd-advocaten.svg" height="56" alt="BVD advocaten"></a></td>
<td align="center" width="25%"><a href="https://www.damste.nl/"><img src="docs/assets/firms/damste.png" height="34" alt="Damsté advocaten - notarissen"></a></td>
<td align="center" width="25%"><a href="https://declercq.com/"><img src="docs/assets/firms/de-clercq.png" height="32" alt="De Clercq Advocaten Notariaat"></a></td>
</tr>
<tr>
<td align="center"><a href="https://deroos.eu/"><img src="docs/assets/firms/de-roos.png" height="30" alt="De Roos"></a></td>
<td align="center"><img src="docs/assets/firms/dm-advocaten.png" height="44" alt="DM Advocaten, Belastingadviseurs, Mediators"></td>
<td align="center"><a href="https://www.holla.nl/"><img src="docs/assets/firms/holla-legal-tax-blue.jpg" height="44" alt="Holla legal &amp; tax"></a></td>
<td align="center"><a href="https://www.hvglaw.nl/"><img src="docs/assets/firms/hvg-law.svg" height="54" alt="HVG Law"></a></td>
</tr>
<tr>
<td align="center"><a href="https://ploum.nl/"><img src="docs/assets/firms/ploum.svg" height="42" alt="Ploum I Rotterdam Law Firm"></a></td>
<td align="center"><a href="https://www.thedatalawyers.com/"><img src="docs/assets/firms/the-data-lawyers.png" height="42" alt="The Data Lawyers"></a></td>
<td align="center"><a href="https://www.vaneps.com/"><img src="docs/assets/firms/vaneps.png" height="22" alt="VANEPS"></a></td>
<td align="center"><a href="https://www.wijnenstael.nl/"><img src="docs/assets/firms/wijn-en-stael.png" height="56" alt="Wijn & Stael Advocaten"></a></td>
</tr>
</table>

## Citeren

Gebruik je DELTA in je onderzoek, citeer het dan als:

```bibtex
@misc{delta_2026,
  title        = {Dutch Legal AI Benchmark (DELTA)},
  author       = {{Legal Benchmarks} and {Zeno.Law}},
  year         = {2026},
  howpublished = {\url{https://github.com/legalbenchmarks/delta}},
  note         = {Version 1.1.0}
}
```
