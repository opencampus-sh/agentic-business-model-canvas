---
name: show-canvas
description: Zeigt das aktuelle Canvas als Seite im Browser, aufgebaut wie das gedruckte Canvas, mit markierten leeren Blöcken und Entscheidungen, die neuer sind als das Canvas. Mit „live“ aktualisiert sich die Seite laufend.
disable-model-invocation: true
---

# Canvas anzeigen

Erzeuge aus dem Canvas eine HTML-Seite mit [`scripts/render_canvas.py`](scripts/render_canvas.py). Das Skript braucht nur die Canvas-Grammatik (`## Abschnitt`-Spalten zwischen `---`-Linien, Blöcke als `### N. Block 👤|🤖`).

## 1. Seite erzeugen

Suche in `AGENTS.md` den Abschnitt, den dieses Skillset angelegt hat (den mit der Zeile `- Canvas:`). Führe das Skript auf diesem Canvas aus, mit der Sprache aus der Zeile `- Language:` (Standard `de`):

```
python3 <skill dir>/scripts/render_canvas.py <canvas> --lang de --out build/canvas.html
```

Liegt `DECISIONS.md` neben dem Canvas, liest das Skript es mit (sonst `--decisions <datei>`). Steht `build/` nicht in `.gitignore`, sag es und biete an, es einzutragen: Die Seite ist nur eine Ansicht, das Canvas bleibt die Quelle.

Mit **live** nach dem Befehl: füge `--watch` hinzu und starte das Skript im Hintergrund. Es erzeugt die Seite bei jeder Änderung an Canvas oder Entscheidungslog neu, und die geöffnete Seite lädt sich alle paar Sekunden neu. Sag, wie man es beendet.

Fertig, wenn die Seite existiert und der Pfad genannt ist (oder sie in einem Browser-Fenster offen ist, falls dein Agent eines hat).

## 2. Auf das Wichtigste hinweisen

In höchstens drei Zeilen, anhand der Markierungen auf der Seite:

- **Leere Blöcke** (gestrichelt, „Noch nicht entschieden“ / „Noch nicht entworfen“), mit Nummer. Ein leerer 👤-Block ist eine Entscheidung, die noch niemand getroffen hat; empfiehl den Skill, der ihn füllt, so wie es der Router-Skill des Skillsets täte.
- **Entscheidungen, die neuer sind als das Canvas** (gemessen am Datum unter *Version*): Die betroffenen Blöcke sind vielleicht veraltet. Biete an, sie zu aktualisieren; wer den Block verantwortet, bestätigt jede Änderung.
- **Offene Fragen** ohne Zuständige oder Termin.

Ändere das Canvas in diesem Skill nur nach einem Ja. Behandle die Seite wie das Canvas selbst: Sie bleibt dort, wo das Canvas liegt, und wird nirgendwo anders veröffentlicht.
