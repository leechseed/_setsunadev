---
original_path: "/mnt/user-data/outputs/truck-pull-list.jsx"
source_conversation: "TRUCK"
created: 2026-04-09
trunk: BLACK
kind: generated-file
---

import { useState, useRef } from "react";

const STATUS = {
  GOOD: { label: "Good", emoji: "✅", color: "#22c55e", bg: "#052e16" },
  ORDER: { label: "Order", emoji: "🛒", color: "#f97316", bg: "#431407" },
  CHECK: { label: "Check", emoji: "❓", color: "#facc15", bg: "#422006" },
};

const emptyForm = { item: "", qty: "", status: "ORDER" };

export default function TruckPullList() {
  const [entries, setEntries] = useState([]);
  const [form, setForm] = useState(emptyForm);
  const [copied, setCopied] = useState(false);
  const [editId, setEditId] = useState(null);
  const itemRef = useRef();

  const handleAdd = () => {
    if (!form.item.trim()) return;
    if (editId !== null) {
      setEntries((prev) =>
        prev.map((e) => (e.id === editId ? { ...form, id: editId } : e))
      );
      setEditId(null);
    } else {
      setEntries((prev) => [...prev, { ...form, id: Date.now() }]);
    }
    setForm(emptyForm);
    itemRef.current?.focus();
  };

  const handleEdit = (entry) => {
    setForm({ item: entry.item, qty: entry.qty, status: entry.status });
    setEditId(entry.id);
    itemRef.current?.focus();
  };

  const handleDelete = (id) => {
    setEntries((prev) => prev.filter((e) => e.id !== id));
    if (editId === id) {
      setEditId(null);
      setForm(emptyForm);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") handleAdd();
  };

  const buildCopyText = () => {
    const date = new Date().toLocaleDateString("en-US", {
      weekday: "short", month: "short", day: "numeric",
    });
    const sections = ["ORDER", "CHECK", "GOOD"]
      .map((key) => {
        const group = entries.filter((e) => e.status === key);
        if (!group.length) return null;
        const header = `── ${STATUS[key].label.toUpperCase()} ${STATUS[key].emoji} ──`;
        const rows = group.map((e) =>
          `  ${e.item}${e.qty ? ` (${e.qty})` : ""}`
        );
        return [header, ...rows].join("\n");
      })
      .filter(Boolean);
    return `TRUCK PULL LIST — ${date}\n\n${sections.join("\n\n")}`;
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(buildCopyText()).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  };

  const grouped = ["ORDER", "CHECK", "GOOD"].map((key) => ({
    key,
    items: entries.filter((e) => e.status === key),
  })).filter((g) => g.items.length);

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0a0a0a",
      fontFamily: "'Courier New', monospace",
      color: "#e5e5e5",
      padding: "24px 16px",
      maxWidth: 540,
      margin: "0 auto",
    }}>
      {/* Header */}
      <div style={{ marginBottom: 28 }}>
        <div style={{
          fontSize: 11, letterSpacing: 4, color: "#555", textTransform: "uppercase", marginBottom: 4,
        }}>
          Vendor Truck Pull
        </div>
        <div style={{ fontSize: 26, fontWeight: 700, color: "#fff", letterSpacing: -1 }}>
          📋 Pull List
        </div>
      </div>

      {/* Input Form */}
      <div style={{
        background: "#141414",
        border: "1px solid #2a2a2a",
        borderRadius: 10,
        padding: 16,
        marginBottom: 20,
      }}>
        {editId !== null && (
          <div style={{ fontSize: 11, color: "#f97316", letterSpacing: 2, marginBottom: 10 }}>
            ✏️ EDITING ITEM
          </div>